from django.db import models

class identitas(models.Model):
    nama_identitas = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama_identitas}"

class Biodata(models.Model):
    identitas = models.ForeignKey(identitas, on_delete=models.CASCADE)
    npm = models.CharField(max_length=100)
    jurusan = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.npm} {self.jurusan}"