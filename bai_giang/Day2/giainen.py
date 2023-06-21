import zipfile
zip_ref=zipfile.ZipFile("../../Data/AI/file_zip/pizza_steak.zip")
zip_ref.extractall()
zip_ref.close()