from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# ユーザー種別の選択肢
USER_ROLE_CHOICES = [
    ('general', '一般'),
    ('manager', '管理者'),
    ('director', '責任者'),
]


class CustomUser(AbstractUser):
    """カスタムユーザーモデル"""
    role = models.CharField(
        'ユーザー種別',
        max_length=20,
        choices=USER_ROLE_CHOICES,
        default='general'
    )
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def is_director(self):
        """責任者かどうか"""
        return self.role == 'director'

    def is_manager(self):
        """管理者かどうか（責任者も含む）"""
        return self.role in ['manager', 'director']

    def is_admin(self):
        """管理画面にアクセスできるか（責任者・管理者）"""
        return self.role in ['manager', 'director']


class Company(models.Model):
    """取引先会社モデル"""
    company_code = models.CharField(
        '会社コード',
        max_length=20,
        unique=True,
        validators=[RegexValidator(regex=r'^[A-Z0-9]+$', message='会社コードは英数字のみです')]
    )
    company_name = models.CharField('会社名', max_length=100)
    contact_person = models.CharField('担当者名', max_length=100)
    address = models.CharField('番地', max_length=200)
    postal_code = models.CharField('郵便番号', max_length=10)
    prefecture = models.CharField('都道府県', max_length=50)
    phone = models.CharField('電話番号', max_length=20)
    email = models.EmailField('メールアドレス')
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = '取引先会社'
        verbose_name_plural = '取引先会社'
        ordering = ['company_code']

    def __str__(self):
        return f"{self.company_code} - {self.company_name}"


class InvoiceItemTemplate(models.Model):
    """請求書項目テンプレートモデル"""
    name = models.CharField('項目名', max_length=100)
    description = models.TextField('説明', blank=True, null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)

    class Meta:
        verbose_name = '請求書項目テンプレート'
        verbose_name_plural = '請求書項目テンプレート'
        ordering = ['name']

    def __str__(self):
        return self.name


class Invoice(models.Model):
    """請求書モデル"""
    invoice_number = models.CharField('請求書番号', max_length=50, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='取引先会社')
    customer_id = models.CharField('顧客ID', max_length=50)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='作成者'
    )

    class Meta:
        verbose_name = '請求書'
        verbose_name_plural = '請求書'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.invoice_number} - {self.company.company_name}"


class InvoiceDetail(models.Model):
    """請求書明細モデル"""
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name='details',
        verbose_name='請求書'
    )
    item_name = models.CharField('請求内容', max_length=100)
    quantity = models.IntegerField('個数', default=1)
    unit_price = models.DecimalField('単価', max_digits=10, decimal_places=2)
    amount = models.DecimalField('金額', max_digits=10, decimal_places=2)
    order = models.IntegerField('順序', default=0)

    class Meta:
        verbose_name = '請求書明細'
        verbose_name_plural = '請求書明細'
        ordering = ['order']

    def __str__(self):
        return f"{self.invoice.invoice_number} - {self.item_name}"

    def save(self, *args, **kwargs):
        """金額を自動計算"""
        self.amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)
