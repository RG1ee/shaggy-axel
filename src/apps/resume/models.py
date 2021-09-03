from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


User = get_user_model()
COURSE_CHOICES = (
    ('BS', 'Bachelor of Science'),
    ('BA', 'Bachelor of Arts'),
    ('BFA', 'Bachelor of Fine Arts'),
    ('BBA', 'Bachelor of Business Administration'),
    ('MS', 'Master of Science'),
    ('MBA', 'Master of Business Administration'),
    ('MFA', 'Master of Fine Arts'),
    ('PHD', 'Ph.D.'),
)


class SkillCategory(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'skill_category'
        verbose_name = 'Category of Skill'
        verbose_name_plural = 'Categories of Skills'


class Skill(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(
        SkillCategory, on_delete=models.DO_NOTHING,
        null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'skills'
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Resume(models.Model):
    about = models.TextField(_('About Me'), max_length=500)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(_('Grade'), max_length=100)
    skills = models.ManyToManyField(Skill)

    @property
    def job_time(self):
        days = sum(job.job_time.days for job in self.job_set.all())
        month = 0
        years = 0

        while days > 30:
            days -= 30
            month += 1
        while month > 12:
            month -= 12
            years += 1

        worked = f'{years}y. {month}m. {days}d.'
        worked = worked.replace('0y. ', '')
        worked = worked.replace('0m. ', '')
        worked = worked.replace('0d.', '')
        if not worked:
            return 'Without Expirience'
        return worked

    def __str__(self):
        return f"{self.applicant.full_name} - {self.job_time}"

    class Meta:
        db_table = 'resume'
        verbose_name = 'Resume'
        verbose_name_plural = 'Resume'


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    school = models.CharField(_('School'), max_length=100)
    course = models.CharField(
        _('Grade'),
        choices=COURSE_CHOICES,
        max_length=100)

    start_date = models.DateField()
    end_date = models.DateField()

    @property
    def education_time(self):
        return (self.end_date - self.start_date)

    def __str__(self):
        return f"{self.school} - {self.course}"

    class Meta:
        db_table = 'education'
        verbose_name = 'Education'
        verbose_name_plural = 'Education'


class Job(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    position = models.CharField(_('Position'), max_length=100)
    company = models.CharField(_('Company'),max_length=100)
    stack = models.ManyToManyField(Skill)
    start_date = models.DateField()
    end_date = models.DateField()

    @property
    def job_time(self):
        return (self.end_date - self.start_date)

    def __str__(self):
        return f"{self.company} \n {self.position} \n {self.job_time}"

    class Meta:
        db_table = 'job'
        verbose_name = 'Job'
        verbose_name_plural = 'Job'


class Portfolio(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    title = models.CharField(_('Project Title'), max_length=100)
    description = models.TextField(_('Description'))
    stack = models.ManyToManyField(Skill, blank=True, symmetrical=False)
    photo = models.ImageField(_('Photo'), upload_to='portfolio/', default='default/project.jpg')
    github = models.URLField(_('GitHub'), blank=True, null=True)
    link = models.URLField(_('Web'), blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.description[:10]} . . ."

    class Meta:
        db_table = 'portfolio'            
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
