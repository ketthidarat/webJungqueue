# Generated by Django 2.2.7 on 2021-01-09 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farmer_name', models.CharField(max_length=1000, verbose_name='ชื่อ-สกุล')),
                ('image', models.ImageField(upload_to='media/', verbose_name='รูปโปรไฟล์')),
                ('address', models.CharField(max_length=1000, verbose_name='ที่อยู่')),
                ('phone', models.CharField(max_length=1000, verbose_name='เบอร์โทรศัพท์')),
                ('email', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'เกษตรกร',
            },
        ),
        migrations.CreateModel(
            name='Money_status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('money_status', models.CharField(max_length=100, verbose_name='สถานะการชำระเงิน')),
            ],
            options={
                'verbose_name': 'สถานะการชำระเงิน',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=1000, verbose_name='ชื่อ-สกุล')),
                ('image', models.ImageField(upload_to='media/', verbose_name='รูปโปรไฟล์')),
                ('address', models.CharField(max_length=1000, verbose_name='ที่อยู่')),
                ('phone', models.CharField(max_length=1000, verbose_name='เบอร์โทรศัพท์')),
                ('email', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'เจ้าของรถ',
            },
        ),
        migrations.CreateModel(
            name='Rice_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rice_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'ลักษณะข้าวที่จะให้เกี่ยว',
            },
        ),
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tractor', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'รถเกี่ยวนวดข้าว',
            },
        ),
        migrations.CreateModel(
            name='Tractor_status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tractor_status', models.CharField(max_length=1000, verbose_name='สถานะรถเกี่ยวนวดข้าว')),
            ],
            options={
                'verbose_name': 'สถานะรถเกี่ยวนวดข้าว',
            },
        ),
        migrations.CreateModel(
            name='Work_status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('work_status', models.CharField(max_length=100, verbose_name='สถานะงาน')),
            ],
            options={
                'verbose_name': 'สถานะงาน',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lat', models.CharField(max_length=1000, verbose_name='ละติจูด')),
                ('lng', models.CharField(max_length=1000, verbose_name='ลองติจูด')),
                ('area', models.IntegerField(verbose_name='พืนที่ (ตรว)')),
                ('other', models.CharField(max_length=1000, verbose_name='อื่นๆ')),
                ('workDetail', models.CharField(max_length=1000, verbose_name='รายละเอียดงาน')),
                ('RepairTime', models.CharField(max_length=1000, verbose_name='เวลาที่ใช้ซ่อมรถ (ชม.)')),
                ('Harverstime', models.CharField(max_length=1000, verbose_name='เวลาที่ใช้เก็บเกี่ยว (ชม.)')),
                ('date_start', models.DateTimeField(verbose_name='วันที่เริ่มเก็บเกี่ยว')),
                ('date_end', models.DateTimeField(verbose_name='วันสิ้นสุดการเก็บเกี่ยว')),
                ('money', models.IntegerField(verbose_name='จำนวนเงิน (บาท)')),
                ('farmer_name', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Farmer', verbose_name='เกษตรกร')),
                ('money_status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Money_status', verbose_name='สถานะการชำระเงิน')),
                ('rice_type', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Rice_type', verbose_name='ลักษณะข้าวที่จะให้เกี่ยว')),
                ('tractor', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Tractor', verbose_name='รถเกี่ยวนวดข้าว')),
                ('tractor_status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Tractor_status', verbose_name='สถานะรถเกี่ยวนวดข้าว')),
                ('work_status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Work_status', verbose_name='สถานะงาน')),
            ],
            options={
                'verbose_name': 'งานที่ต้องเก็บเกี่ยว',
            },
        ),
        migrations.AddField(
            model_name='tractor',
            name='tractor_status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Tractor_status'),
        ),
    ]
