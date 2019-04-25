# Generated by Django 2.1 on 2019-04-25 20:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mugshot', models.ImageField(default='/static/upload/mugshots/default.jpg', upload_to='upload/mugshots', verbose_name='头像')),
                ('phone', models.CharField(blank=True, max_length=12, verbose_name='手机号')),
                ('nickname', models.CharField(blank=True, max_length=20, verbose_name='昵称')),
                ('department', models.CharField(blank=True, max_length=20, verbose_name='所在学院')),
                ('sex', models.CharField(blank=True, max_length=2, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('introduce', models.CharField(blank=True, max_length=254, verbose_name='个人介绍')),
                ('blog', models.CharField(blank=True, max_length=20, verbose_name='博客/github')),
                ('last_login', models.DateField(default=django.utils.timezone.now, verbose_name='最近登录')),
                ('skill', models.CharField(blank=True, max_length=100, verbose_name='技能')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('permissions', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(default='', max_length=250)),
                ('is_official', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('apply_end', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_contests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '竞赛',
                'verbose_name_plural': '竞赛',
                'db_table': 'contest',
            },
        ),
        migrations.CreateModel(
            name='ContestApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applies', to='common.Contest')),
            ],
            options={
                'verbose_name': '比赛报名表',
                'verbose_name_plural': '比赛报名表',
                'db_table': 'contest_apply',
            },
        ),
        migrations.CreateModel(
            name='ContestCommitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
                ('result', models.CharField(default='', max_length=20, verbose_name='结果')),
                ('cost_time', models.IntegerField(default=-1, verbose_name='时间消耗')),
                ('cost_memory', models.IntegerField(default=-1, verbose_name='内存消耗')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
                ('code', models.TextField(verbose_name='代码')),
                ('language', models.CharField(default='N/A', max_length=15)),
                ('is_simulation', models.IntegerField(default=False, verbose_name='是否模拟')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='common.Contest', verbose_name='比赛')),
            ],
            options={
                'verbose_name': '比赛提交记录',
                'verbose_name_plural': '比赛提交记录',
                'db_table': 'group_commit_record',
            },
        ),
        migrations.CreateModel(
            name='ContestGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('time_cost', models.TimeField(default=(1900, 1, 1, 0, 0, 0, 0, 1, -1))),
                ('is_simulation', models.IntegerField(default=False, verbose_name='是否模拟')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='common.Contest')),
            ],
            options={
                'verbose_name': '竞赛成绩',
                'verbose_name_plural': '竞赛成绩',
                'db_table': 'contest_grade',
            },
        ),
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发表时间')),
                ('star', models.BigIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubts', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '帖子',
                'verbose_name_plural': '帖子',
                'db_table': 'doubt',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='DoubtComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('visible', models.BooleanField(default=True, verbose_name='是否可见')),
                ('star', models.IntegerField(default=0, verbose_name='点赞')),
                ('is_private', models.BooleanField(default=False, verbose_name='是否私有')),
                ('is_parent_comment', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubtcomment', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('doubt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='common.Doubt', verbose_name='帖子')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_comments', to='common.DoubtComment', verbose_name='上级评论')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubtcomment_replied', to=settings.AUTH_USER_MODEL, verbose_name='回复')),
            ],
            options={
                'verbose_name': '帖子评论',
                'verbose_name_plural': '帖子评论',
                'db_table': 'doubt_comment',
                'ordering': ['-created_time'],
                'get_latest_by': 'created_time',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduce', models.CharField(blank=True, max_length=254)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='题目')),
                ('content', models.TextField(verbose_name='描述')),
                ('time_limited', models.IntegerField(default=1000, verbose_name='时间限制')),
                ('memory_limited', models.IntegerField(default=65536, verbose_name='空间限制')),
                ('rank', models.IntegerField(verbose_name='等级')),
                ('in_description', models.TextField(verbose_name='输入描述')),
                ('out_description', models.TextField(verbose_name='输出描述')),
                ('in_case', models.TextField(verbose_name='样例输入')),
                ('out_case', models.TextField(verbose_name='样例输出')),
                ('source', models.CharField(max_length=254, verbose_name='来源')),
                ('tip', models.TextField(verbose_name='提示')),
                ('visible', models.BooleanField(default=True, verbose_name='是否显示')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_modify', models.DateTimeField(auto_now_add=True)),
                ('contest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='common.Contest')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_problems', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '题库',
                'verbose_name_plural': '题库',
                'db_table': 'problem',
            },
        ),
        migrations.CreateModel(
            name='ProblemComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('visible', models.BooleanField(default=True, verbose_name='是否可见')),
                ('star', models.IntegerField(default=0, verbose_name='点赞')),
                ('is_private', models.BooleanField(default=False, verbose_name='是否私有')),
                ('is_parent_comment', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problemcomment', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_comments', to='common.ProblemComment', verbose_name='上级评论')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='common.Problem', verbose_name='问题')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problemcomment_replied', to=settings.AUTH_USER_MODEL, verbose_name='回复')),
            ],
            options={
                'verbose_name': '问题评论',
                'verbose_name_plural': '问题评论',
                'db_table': 'problem_comment',
                'ordering': ['-created_time'],
                'get_latest_by': 'created_time',
            },
        ),
        migrations.CreateModel(
            name='ProblemCommitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
                ('result', models.CharField(default='', max_length=20, verbose_name='结果')),
                ('cost_time', models.IntegerField(default=-1, verbose_name='时间消耗')),
                ('cost_memory', models.IntegerField(default=-1, verbose_name='内存消耗')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
                ('code', models.TextField(verbose_name='代码')),
                ('language', models.CharField(default='N/A', max_length=15)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problemcommitrecord', to='common.Problem', verbose_name='题目编号')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '问题提交记录',
                'verbose_name_plural': '问题提交记录',
                'db_table': 'user_commit_record',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(related_name='problems', to='common.Tag'),
        ),
        migrations.AddField(
            model_name='doubt',
            name='tags',
            field=models.ManyToManyField(related_name='doubts', to='common.Tag'),
        ),
        migrations.AddField(
            model_name='contestgrade',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='common.Group'),
        ),
        migrations.AddField(
            model_name='contestcommitrecord',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='common.Group', verbose_name='队伍'),
        ),
        migrations.AddField(
            model_name='contestcommitrecord',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contestcommitrecord', to='common.Problem', verbose_name='题目编号'),
        ),
        migrations.AddField(
            model_name='contestapply',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applies', to='common.Group'),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='common.Group'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
