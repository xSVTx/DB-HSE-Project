# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.urls import reverse


class Assignment(models.Model):
    ASSIGNMENT_STATUS = [
        ('N', "Not started"),
        ('I', "In process"),
        ('D', "Done")
    ]
    assignment_id = models.IntegerField(primary_key=True)
    assignmentinfo = models.TextField(blank=True, null=True)
    assignmentdeadline = models.DateField(blank=True, null=True)
    assignmentstatus = models.CharField(choices=ASSIGNMENT_STATUS, max_length=18, blank=True, null=True)
    lectures = ManyToManyField('Lectures')

    def get_absolute_url(self):
        return reverse("dbapp:assignment-detail", kwargs={"id": self.assignment_id})

    class Meta:
        indexes = [
            models.Index(fields=['assignmentinfo'])
        ]
        db_table = 'assignment'


class Courses(models.Model):
    course_id = models.IntegerField(primary_key=True)
    coursename = models.CharField(max_length=50)
    coursestartdate = models.DateField()
    courseenddate = models.DateTimeField(blank=True, null=True)
    assignmentsnum = models.IntegerField(blank=True, null=True)
    materialsnum = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("dbapp:course-detail", kwargs={"id": self.course_id})

    class Meta:
        indexes = [
            models.Index(fields=['coursename'])
        ]
        db_table = 'courses'


# class CoursesTeacher(models.Model):
#     teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, blank=True, null=True)
#     course = models.ForeignKey('Courses', on_delete=models.CASCADE)

#     class Meta:

#         db_table = 'courses_teacher'


class Exams(models.Model):
    exam_id = models.IntegerField(primary_key=True)
    examdate = models.DateTimeField()
    examtimestart = models.TimeField()
    examtimeend = models.TimeField()
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("dbapp:exam-detail", kwargs={"id": self.exam_id})

    class Meta:
        indexes = [
            models.Index(fields=['examdate'])
        ]
        db_table = 'exams'


class Lectures(models.Model):
    LECTURE_FORMAT = [
        ('ON', 'Online'),
        ('OFF', 'Offline')
    ]
    lecture_id = models.IntegerField(primary_key=True)
    lecturesname = models.TextField(blank=True, null=True)
    lectureformat = models.CharField(choices=LECTURE_FORMAT, max_length=9, blank=True, null=True)
    lecturedate = models.DateTimeField()
    lecturetimestart = models.TimeField()
    lecturetimeend = models.TimeField()
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    recording = models.ForeignKey('Recordings', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("dbapp:lecture-detail", kwargs={"id": self.lecture_id})

    class Meta:
        indexes = [
            models.Index(fields=['lecturesname'])
        ]
        db_table = 'lectures'


# class LecturesAssignement(models.Model):
#     assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE, blank=True, null=True)
#     lecture = models.ForeignKey('Lectures', on_delete=models.CASCADE, blank=True, null=True)

#     class Meta:

#         db_table = 'lectures_assignement'


class Materials(models.Model):
    material_id = models.IntegerField(primary_key=True)
    materialinfo = models.TextField(blank=True, null=True)
    materiallink = models.TextField(blank=True, null=True)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("dbapp:material-detail", kwargs={"id": self.material_id})

    
    def save(self, *args, **kwargs):
        
        print(self._state.adding)
        if self._state.adding is True:
            check = []
            print(self.material_id)
            tempCourse = Courses.objects.get(course_id=self.course.course_id)
            if tempCourse not in check:
                check.append(tempCourse)
                if tempCourse.materialsnum is None:
                    print('Were in here')
                    tempCourse.materialsnum = 1
                else:
                    print('Were not there')
                    tempCourse.materialsnum += 1
                tempCourse.save()
        else:
            tempMat = Materials.objects.get(material_id=self.material_id)
            tempCoursePre = Courses.objects.get(course_id=tempMat.course.course_id)
            tempCoursePost = Courses.objects.get(course_id=self.course.course_id)
            if tempCoursePre != tempCoursePost:
                tempCoursePre.materialsnum -= 1
                tempCoursePre.save()
                if tempCoursePost.materialsnum is None:
                    print('Were in here')
                    tempCoursePost.materialsnum = 1
                else:
                    print('Were not there')
                    tempCoursePost.materialsnum += 1
                tempCoursePost.save()


        super(Materials, self).save(*args, **kwargs)


    def delete(self, *args, **kwargs):

        tempAss = Materials.objects.get(material_id=self.material_id)
        check = []
        print(self.material_id)
        print(tempAss.course)
        tempCourse = Courses.objects.get(course_id=tempAss.course.course_id)
        if tempCourse not in check:
            check.append(tempCourse)
            if tempCourse.materialsnum is not None:
                print('Were in here')
                tempCourse.materialsnum -= 1
            tempCourse.save()

        return super(Materials, self).delete()


    class Meta:
        indexes = [
            models.Index(fields=['materialinfo'])
        ]
        db_table = 'materials'

class Recordings(models.Model):
    recording_id = models.IntegerField(primary_key=True)
    recordingURL = models.TextField(blank=True, null=True)
    lecture = models.ForeignKey('Lectures', on_delete=models.CASCADE)

    def get_absolute_url(self):
            return reverse("dbapp:recording-detail", kwargs={"id": self.recording_id})

    class Meta:

        db_table = 'recordings'

class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacherfullname = models.TextField(blank=True, null=True)
    teachertel = models.TextField(blank=True, null=True)
    teachermail = models.EmailField(max_length = 254, blank=True, null=True)
    exam = models.ForeignKey('Exams', on_delete=models.CASCADE, blank=True, null=True)
    courses = ManyToManyField('Courses')

    def get_absolute_url(self):
            return reverse("dbapp:teacher-detail", kwargs={"id": self.teacher_id})

    class Meta:
        indexes = [
            models.Index(fields=['teacherfullname'])
        ]
        db_table = 'teacher'

