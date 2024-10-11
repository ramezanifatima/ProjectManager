from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from Projects.models import Project, Task, SubTask


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('Manager', 'Manager'),
        ('Owner', 'Owner'),
        ('Viewer', 'Viewer'),
        ('Developer', 'Developer')
    )
    phone_number = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=9, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']
    objects = UserManager()

    def __str__(self):
        return f'{self.phone_number}--{self.role}'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, unique=True)
    image = models.ImageField(upload_to='accounts/profile/',
                              default='accounts/profile/default/default_avatar.jpg')

    def __str__(self):
        return self.user.phone_number

    # @property
    # def all_project(self):
    #     count = 0
    #     all_pj = Project.objects.filter(user=self.user)
    #     for pj in all_pj:
    #         count += 1
    #     return count
    #
    # @property
    # def all_task(self):
    #     count = 0
    #     all_task = Task.objects.filter(project__user=self.user)
    #     for task in all_task:
    #         count += 1
    #     return count
    #
    # @property
    # def all_sub_task(self):
    #     count = 0
    #     all_sub = SubTask.objects.filter(task__project__user=self.user)
    #     for sub in all_sub:
    #         count += 1
    #     return count
    #
    # @property
    # def count_project(self):
    #     if self.all_project != 0:
    #         count = 0
    #         done = 0
    #         all_pj = Project.objects.filter(user=self.user)
    #         for pj in all_pj:
    #             count += 1
    #             if pj.status is True:
    #                 done += 1
    #         avg = (done / count)
    #         percentage = avg * 100
    #         return int(percentage)
    #     else:
    #         return 0
    #
    # @property
    # def count_task(self):
    #     if self.all_task != 0:
    #         count = 0
    #         done = 0
    #         all_task = Task.objects.filter(project__user=self.user)
    #         for task in all_task:
    #             count += 1
    #             if task.status is True:
    #                 done += 1
    #         avg = (done / count)
    #         percentage = avg * 100
    #         return int(percentage)
    #     else:
    #         return 0
    #
    # @property
    # def count_sub_task(self):
    #     if self.all_sub_task != 0:
    #         count = 0
    #         done = 0
    #         all_sub = SubTask.objects.filter(task__project__user=self.user)
    #         for sub in all_sub:
    #             count += 1
    #             if sub.status is True:
    #                 done += 1
    #
    #         avg = (done / count)
    #         percentage = avg * 100
    #         return int(percentage)
    #     else:
    #         return 0
