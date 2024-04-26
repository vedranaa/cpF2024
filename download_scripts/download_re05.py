import os
import sys

if not os.path.exists(os.path.join(os.getcwd(), "cp")):
    print("Oh no, you are not in the 02002students folder.")
    print("Please open the 02002students folder in VS code and run the script again.")
    sys.exit(1) # Exit with error code 1

try:
    import unitgrade # type: ignore
    import dtumathtools # type: ignore
except ImportError as e:
    print("Oh no, Python encountered a problem during importing unitgrade")
    print("This means that your current python has never had the cp package installed.")
    print("Please select a different Python through the Command Palette (Ctrl+Shift+P) and choose ""Python: Select Interpreter"".")
    print("Try all the Pythons you can choose and run the script from them")
    print("")
    print("If you have not yet followed step 5 of the installation instructions from week 1 please do so now. Here is a link:")
    print("https://cp.compute.dtu.dk/installation/installation.html#step-5-install-the-course-toolbox-and-software-packages")
    sys.exit(1) # Exit with error code 1
try:
    import cp.ex00 # type: ignore
except ImportError as e:
    print("Oh no, Python encountered a problem during importing cp.") 
    import site
    for site_path in site.getsitepackages():
        egg_path = os.path.join(site_path, "cp.egg-link")
        if os.path.exists(egg_path):
            with open(egg_path, "r") as f:
                print("It tried looking in the following folder, but could not find the cp package there:")
                print(f.read())
    print("")
    print("This most likely means that you have moved or renamed the 02002students folder since following step 5 of the installation guide.")
    print("Please move/rename the students folder back so it can be found at the this path again")
    print("If you have tried running the script with EVERY Python interpreter, and this does still not work, make sure you have followed the installation instructions from week 1. Here is a link:")
    print("https://cp.compute.dtu.dk/installation/installation.html#step-5-install-the-course-toolbox-and-software-packages")
    sys.exit(1) # Exit with error code 1

cp_path = os.path.dirname(cp.__file__)

print("cp folder located at", cp_path)
assert "02002public" not in cp_path, "Probably running on the lecturer's computer, don't do that."

import base64
import io
import zipfile

# Replace this with your base64-encoded string


def add_new_files(encoded_zip_data):
    # Decode the base64 string to binary data
    zip_binary_data = base64.b64decode(encoded_zip_data)

    # Create an in-memory file-like object from the binary data
    zip_file_like = io.BytesIO(zip_binary_data)

    # You can now work with the zip file in memory
    with zipfile.ZipFile(zip_file_like, 'r') as zip_file:
        
        # Iterate over the file list
        for file in zip_file.namelist():
            if file == '.gitignore' or file.endswith('/'):
                continue
            assert file.startswith('cp/'), file

            # Extract the file from the zip archive (for example, the first file)
            file_content = zip_file.read(file)
            out_path = os.path.join(cp_path, file[3:])

            # Make sure we don't overwrite files that are already there, except for tests
            if (not os.path.exists(out_path)) or (file.startswith('cp/tests/')) or (file.startswith('cp/project')):
                os.makedirs(os.path.dirname(out_path), exist_ok=True)

                # Check if the file is already up to date
                if (os.path.exists(out_path)):
                    with open(out_path, "rb") as existing_file:
                        # Replace Windows line endings with Unix line endings
                        existing_content = existing_file.read().replace(b'\r\n', b'\n')
                    if existing_content == file_content:
                        continue
                # Write the file to disk
                with open(out_path, 'wb') as f:
                    f.write(file_content)
                    print("Writing to", out_path)

    # We don't need the binary data anymore, and close the in-memory file-like object
    zip_file_like.close()
    print("Files are up to date")
    print()
    print("Successfully completed!")

# Run the function on the base64-encoded version of the zip file
add_new_files("""UEsDBAoAAAAAAPCWmVgAAAAAAAAAAAAAAAADAAkAY3AvVVQFAAEEiypmUEsDBAoAAAAAAPCWmVgAAAAAAAAAAAAAAAAIAAkAY3AvcmUwNS9VVAUAAQSLKmZQSwMECgAAAAgA8JaZWH6BVul8AAAAnQAAABAACQBjcC9yZTA1L2Jvb2tzLnB5VVQFAAEEiypmJYyxDsIwEEP3fIUVZjJRhowE5i78wKW9KhGkJ10C4vNJwJNl+9lae/uwLrkyJnc6Tu7scRF5IDypVmutMctwv9AbdPUwKFNjEP5dS9RQmyhX5H0TLdSy7KAor9ZXsbNufA38gPt8nT2CrIxEFZF5h3KRN6/YVAoSKzuYL1BLAwQKAAAACADwlplYl/2hDLsAAACrAQAAHAAJAGNwL3JlMDUvY2hlbWljYWxfcmVhY3Rpb24ucHlVVAUAAQSLKmadkMEKwjAQRO/9iiFe9GChiBdvpXqUgvgD23RLi0kXklT8fNPaghdBmkNYksy8ySilLi92uvPscUyzbB+3wwlFy7bTZHBj0qGTHoUh75VSSZLocUQexG53pwRxxfPCMQUG4XMbWgrwQVz07fpGnKXJhioZAigOUZ5OfqPBBvfyXEau1IyWPCrmHo6tPLlG48SiZccpptdzgqsY1oPhrxT5f3jYWbomwUxfmvlFNyIPH785VrK06WbNGuwbUEsDBAoAAAAIAPCWmVjO7ssfeAAAAJkAAAASAAkAY3AvcmUwNS9jb3VudGVyLnB5VVQFAAEEiypmNY2xDsIwDET3fMXJLLBEAomla2Duwg+k6aFUoqnkBAR/TyyEJ+vdPVtErm9qWipx9qcBYXuWRkV4xFpFxLlk25/vD4NDn54EZWxExK/QcmxYSlKuLK0aNwXTB0dvh0zb4TZeRvsyEzlWTGRBV7YXZ9x1W5Gp9HBfUEsDBAoAAAAIAPCWmVjdCAmzlwAAAMsAAAARAAkAY3AvcmUwNS9lYm9va3MucHlVVAUAAQSLKmYljrEOgzAMRPd8xSld2iViQa0YS5lZ+gMGjEBtYuSkVT+/CXg4S9bdO1trux/ruEZG7a6gMOV9a9DdRV7RWmvMrOIxbk65qt1Qzlj9JppQPMaMb4rxCJyLXBqDPDnbKlNiEA5LWighJlHOhDCLekqrBNAgn5SrwYXuSmkB7HLCs3/0DVqZGAtFDMwByl6+PGF/bWFlB/MHUEsDBAoAAAAIAPCWmVggt3ENoQAAAO8AAAASAAkAY3AvcmUwNS9saWJyYXJ5LnB5VVQFAAEEiypmVY67DsIwDEX3fMVVmInK0IGOlG5IXfgBt3XVCFJXTkDw9/QhhnqzzvXxtdZWH9bWR0buzsfcnbICN98o6Rflk2K01hrTqwS0k1POcteIPCJ8mEQTLvOyx7zj1Row7aL6iwuDeWZxqUyJQdhwGighJlGez8deNFDyMoIaeSVsWho7bB/c0mwRHXCvr3WBUjrGQBEN8wjlIG/usHYbWNnB/ABQSwMECgAAAAgA8JaZWC4GH4SNAAAAvwAAABAACQBjcC9yZTA1L25hbWVzLnB5VVQFAAEEiypmTY2xDsIwDET3fMUpLLBUYmDpWmCkS3dkmqta0aaSkyI+HwcWPNl3987e+8ub2k+JOFXHGjdZmNDMkpL33rm+bLhu83wv1v5QO9iY1yglE4JfJI+SkeVp9BRNHSZNGdEYSAywzN+lzJvGAhGDdX+dqjws5Tt07bmt0ayBGCXhQUZjlvXFgEHXBSOVFdwHUEsDBAoAAAAIAPCWmVjzPrBnggAAAK8AAAAWAAkAY3AvcmUwNS90ZW1wZXJhdHVyZS5weVVUBQABBIsqZk2MMQ7CMBRD95zCCnsXxNI1wNqlF/ikRqnUJujnt3B8GrHgyZL9nvf+9qHGuRKX7txj5Pqiim1KhEVq9d47F1v733qHI8cWlGKE4HexJIZY8k61igftTWYELnHeKiRPuEtS5sTZuqZumhPG4Tr0CGUikjTugJRr2TnhqWVForKD+wJQSwMECgAAAAAA8JaZWAAAAAAAAAAAAAAAAAkACQBjcC90ZXN0cy9VVAUAAQSLKmZQSwMECgAAAAgA8JaZWBurfN6OBgAAaSQAABYACQBjcC90ZXN0cy90ZXN0c19yZTA1LnB5VVQFAAEEiypm3Vpbb6M4FH7Pr7DYhyFahgaSNGmlrjTttNNd7UxXM13tQxUhQ5yCanAGTLedX7+2wQkGQ5ImrUZbqReOz/1859i4WaQkBnkS0fsUzhGI4iVJKfiK+C8L/H2LMnoBM9QrF4Kl/Csi8i8uTRlfbyF18Sc7JsGD1LeENAglP8l6vQDDLGNmBmNv4JgrM/3THmBfQlGwtFO2bicwRplUdJVj7H1hFME3RwvAbXkLTuaMZobwotQiNIEzwEn2StA0/iBhYljA+EiQ0V9xCi7mFErp5fccYnNh36Oq5j4T4aJAldNagAl6qQUmuoWFDzgKhIlvcUTDXY0IaVAX1dk5J/6LrTDZrWxchDDFkYjmPCX/JrvaKeVBXVgBmdsNsoDkCUWphNlF8aiCrOSpQyyQIZVCZof7gXBfKOKuD9asgR0lQYpixFe2VuDsq8DdV8FwXwWjfRWM++o4GXZXmqJ4iVJI83Q17W7XJLXiFd561amsekWYQdlQitpwndqUeAHCQZRnNQDoeRcwTFESoqhIdqVc1M5Q4aHpDHaxuQW3atV1qma1cV8ZqnNvFLji2SsHrhG4l37UeVVAjroB6RPysNrfztmDikG+7Dl1+PmyDFzAND4T/xl8jIIHPkSvURrDBHxG+DHCmM/Vk8l04Izc0XDijiYdIVX1+EV4EcVsyq5l/CL7gmzchgj8E0LcuctVuFqVqtF8RXD+DP7C8JlN5Bu+lRqXacKSAS5wlMiAhoPJdDoZjYZdtmtyhX2Y05Ckzah+/3b+xXQ61DllAIKxX5s74/3L7L5KmSOmxGejdUG6pupaOWC/a8otwEM+VS0YVnT4Em7pbF0/97lqoOrwyopwWC3a8f5FG75Nb/r2gjDZVe9R1lVhntyz+O/5CdnoW6LTrgvap4K2vT6IMSALwFXccopQ+IERb1Simr/JS/KnsCCF57KZZKSfgEhm+bJIM/fxU4ogZaHTzH/m2b6ywbeAUPbaENEfLCsQzzmZp3wyGrqT4fh4zAmOPa6kCjLNqDqo2pMIrabdDnakjB9L61+/NcJdgGR1TUVUGWLWtvgrhBYRRl4W/eAn72ENC9P/IRb0u1lVN588Gt3VAbTSbzEGzF68WP5OATdkoXLUvUnVC1PW7pNe8Xto1IfoyasVXmHCkZ/C9Fly/Vk8qgApeZoQwTKtpZjZunW9GDztNTwcHrEN53Ox75h+nSqSaKI1+Ym5gUXbJnkshLKuYfZkOW2yaDdh3z3EFliN1d0jqlbZHaOqYt4Z/HyYb5weXx3zo58P840S3u0zsUfcm4NO/JmF2bsGTIPQNOSBoa+vZ+Ng2VXPg3TcoQ7xXRVr6WeZE+541/77ZN294E1lVmhUOnjDtXMQojgKIPZY5QMakUT24AdKYrVgkFHqtYIylZzdNK5Zshzlvq55srgG7OWT8WU0NWG/k5NxQTHGEC6vyzRFLC3zOrnKPVtF4W2aI7OmSiCmeo8KGrnbdJvalrvPBKMgx2ivdMelknrKYxm4tFLpj43liAU4RSVhq9gNE5syseMd5Upz7iYxTaVdbjMuzt7sfS3H0KzPC5mP5gbQlZFAdZHfXB4zLys+kl2CD7RUsonajPjixm2LuAHDDVe9rZj6Wj6/NXIlR6NOzl7QdV6K3a0ENeDVy8Xua8PN1ePN1QNOT06lGQkC8y52ZtZd7M42NCJ4/xso0MkndKqf0FcQZ8hMbR9imARoXfJ618qFZte2pcoeOM7GdI3tk5OTStpJZ1GIPqMKnWymh3qI2oPBtMLU5UlYURxuJMeIhjAhuEOhZNEjprFIuhY1lg+8GLqkMzmkTWozvRv6rKIW45ffMwvcSUf5M+nsCdYM4FdwXf0hWuR6JB5uujtFHD30jaIM+Q3/PtnxnOaNdj6p1Q9UjXnYPE9FmRdlhJIlYgfg1iHYfTQrJomiK6huhJUk8fxkZvGhjTIycXXJzBliDbCdFPB0GWLxF/CI0ozn6ox1qVPS8pQ3lBFSusxOj47umQbo2wGJlzlF9pzm9vzhKFgeDdzBwM1oPmenxezo/ZGPiX8Uw4yilC/zVGeFnSUMHryiHBlTfRcsZ4IeJfPoMZozEFVXi7XvOZNnrgnSKlqz/KgI/y9e36qTXT15qCeP9OSxnnysJ0/05KmefKIlOwM9WR+lo4/S0UfpFFGuqPJr1utFC+CJT094Hjg7A+88L4ZR4nnvKt3V+EQQeoQ4h5T3KX/2yvoLiZY1cw1Nhtv/AFBLAwQKAAAAAADwlplYAAAAAAAAAAAAAAAAGAAJAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1VUBQABBIsqZlBLAwQKAAAACADwlplYCM9wAWEAAABwAAAAIwAJAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDEucGtsVVQFAAEEiypma2CZmsoAAbVTNHrYg1INTOMNDKf0cBWnloQWOOckFhdPaZvSw1KSmZsKZLjb6z4Aq85g7OErSS0uiU8rzcmJz0sEy/awAZWnFpUAmbVTMhgz2NqmZLAANdn9PQDWVKoHAFBLAwQKAAAACADwlplY/0x4KWAAAABuAAAAIwAJAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDIucGtsVVQFAAEEiypma2CZmswAAbVTNHrYg1INTOMNjKb0cBWnloQWOOckFhdPaZvSw1KSmZsKZLjbG9wAq85g7OEpSS0uiU/OL80rSS0CKWIDKk4tKgEya6dkMGawtU3JYAFqsftxAKylVA8AUEsDBAoAAAAIAPCWmVizj4rZYQAAAHIAAAAjAAkAY3AvdGVzdHMvdW5pdGdyYWRlX2RhdGEvUmUwNV8wMy5wa2xVVAUAAQSLKmZrYJmazgABtVM0etiDUg1M4w2Mp/RwFaeWhBY45yQWF09pm9LDUpKZmwpkuNubQlRnMPYIlKQWl8SXpOYWpBYllpQWgeR72IAaUotKgMzaKRmMGWxtUzJYQNo4G8DaSvUAUEsDBAoAAAAIAPCWmVhgiuvvXgAAAG0AAAAjAAkAY3AvdGVzdHMvdW5pdGdyYWRlX2RhdGEvUmUwNV8wNC5wa2xVVAUAAQSLKmZrYJmaxAABtVM0etiDUg1M4w1MpvRwFaeWhBY45yQWF09pm9LDUpKZmwpkuNsb1oBVZzD2cJekFpfEJ+XnZ8cbgtSwAdWmFpUAmbVTMhgz2NqmZLCAdDAfAOso1QMAUEsDBAoAAAAIAPCWmViuMwOYXgAAAG0AAAAjAAkAY3AvdGVzdHMvdW5pdGdyYWRlX2RhdGEvUmUwNV8wNS5wa2xVVAUAAQSLKmZrYJmaxAABtVM0etiDUg1M4w1Mp/RwFaeWhBY45yQWF09pm9LDUpKZmwpkuNubeIBVZzD2cJekFpfEJ+XnZ8cbgdSwAdWmFpUAmbVTMhgz2NqmZLCAdDAsAOso1QMAUEsDBAoAAAAIAPCWmVjoa+9ZXwAAAG0AAAAjAAkAY3AvdGVzdHMvdW5pdGdyYWRlX2RhdGEvUmUwNV8wNi5wa2xVVAUAAQSLKmZrYJmaxAABtVM0etiDUg1M4w3MpvRwFaeWhBY45yQWF09pm9LDUpKZmwpkuNsbXACrzmDs4S5JLS6JT8rPz443BqlhA6pNLSoBMmunZDBmsLVNyWAB6rD73wDWUaoHAFBLAwQKAAAACADwlplYvHOIGl8AAABuAAAAIwAJAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDcucGtsVVQFAAEEiypma2CZmswAAbVTNHrYg1INTOMNzKf0cBWnloQWOOckFhdPaZvSw1KSmZsKZLjb6wWAVWcw9vCUpBaXxKcm5ednxxuCFLEBFacWlQCZtVMyGDPY2qZksIC0MB0AaynVAwBQSwMECgAAAAgA8JaZWABkUQFgAAAAbgAAACMACQBjcC90ZXN0cy91bml0Z3JhZGVfZGF0YS9SZTA1XzA4LnBrbFVUBQABBIsqZmtgmZrMAAG1UzR62INSDUzjDSym9HAVp5aEFjjnJBYXT2mb0sNSkpmbCmS422sogFVnMPbwlKQWl8SnJuXnZ8cbghSxARWnFpUAmbVTMhgz2NqmZLAAtdj9PwDWUqoHAFBLAwQKAAAACADwlplYlgWZ72EAAABwAAAAIwAJAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDkucGtsVVQFAAEEiypma2CZmsoAAbVTNHrYg1INTOMNLKf0cBWnloQWOOckFhdPaZvSw1KSmZsKZLjbG6mAVWcw9vCVpBaXxOdkJhUlFlXGG4KUsQGVpxaVAJm1UzIYM9japmSwgDQxHQBrKtUDAFBLAwQKAAAACADwlplYoDKmpG8AAACeAAAAIwAJAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMTAucGtsVVQFAAEEiypma2CZOpkBAmqnaPSwB6UamMYbGkzp4SpOLQktcM5JLC6e0jalh6UkMzcVyHC3D4gFq85g7OErSS0uic/JTCpKLKqMNwIpYwMqTy0qATJrp2QwZrC1TclgAWlibcCuyRioMoMDqpoXqtruD0R1qR4AUEsDBAoAAAAIAPCWmVib+HopXAAAAGsAAAAjAAkAY3AvdGVzdHMvdW5pdGdyYWRlX2RhdGEvUmUwNV8xMS5wa2xVVAUAAQSLKmZrYJmawAABtVM0etiDUg1M4w0Np/RwFaeWhBY45yQWF09pm9LDUpKZmwpkuNvrTgCrzmDs4SxJLS6JTyzJzwWpYAOqTC0qATJrp2QwZrC1TclgAaq3+wkxvVQPAFBLAwQKAAAACADwlplY7fyMo3MAAACeAAAAIwAJAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMTIucGtsVVQFAAEEiypma2CZOpkBAmqnaPSwB6UamMYbGk3p4SpOLQktcM5JLC6e0jalh6UkMzcVyHC319MAq85g7OEtSS0uic/Nz0lNLs0BSfawAVWnFpUAmbVTMhgz2NqmZLCA9Eh+gOnhR9ETbwRUmsEBVc4LVW73qQGsvFQPAFBLAwQKAAAACADwlplYxjG/0HIAAACeAAAAIwAJAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMTMucGtsVVQFAAEEiypma2CZOpkBAmqnaPSwB6UamMYbGk/p4SpOLQktcM5JLC6e0jalh6UkMzcVyHC31+gAq85g7OEtSS0uiS9KTUwuyczPA6liA6pOLSoBMmunZDBmsLVNyWAB6eE/ANPDj6In3gioNIMDqpwXplzAAKy8VA8AUEsDBAoAAAAIAPCWmViG/TlNXgAAAG0AAAAjAAkAY3AvdGVzdHMvdW5pdGdyYWRlX2RhdGEvUmUwNV8xNC5wa2xVVAUAAQSLKmZrYJmaxAABtVM0etiDUg1M4w1NpvRwFaeWhBY45yQWF09pm9LDUpKZmwpkuNub7ACrzmDs4S5JLS6JTyzJz403AalhA6pNLSoBMmunZDBmsLVNyWAB6rB7AzG/VA8AUEsBAgAACgAAAAAA8JaZWAAAAAAAAAAAAAAAAAMACQAAAAAAAAAQAAAAAAAAAGNwL1VUBQABBIsqZlBLAQIAAAoAAAAAAPCWmVgAAAAAAAAAAAAAAAAIAAkAAAAAAAAAEAAAACoAAABjcC9yZTA1L1VUBQABBIsqZlBLAQIAAAoAAAAIAPCWmVh+gVbpfAAAAJ0AAAAQAAkAAAAAAAEAAAAAAFkAAABjcC9yZTA1L2Jvb2tzLnB5VVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWJf9oQy7AAAAqwEAABwACQAAAAAAAQAAAAAADAEAAGNwL3JlMDUvY2hlbWljYWxfcmVhY3Rpb24ucHlVVAUAAQSLKmZQSwECAAAKAAAACADwlplYzu7LH3gAAACZAAAAEgAJAAAAAAABAAAAAAAKAgAAY3AvcmUwNS9jb3VudGVyLnB5VVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWN0ICbOXAAAAywAAABEACQAAAAAAAQAAAAAAuwIAAGNwL3JlMDUvZWJvb2tzLnB5VVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWCC3cQ2hAAAA7wAAABIACQAAAAAAAQAAAAAAigMAAGNwL3JlMDUvbGlicmFyeS5weVVUBQABBIsqZlBLAQIAAAoAAAAIAPCWmVguBh+EjQAAAL8AAAAQAAkAAAAAAAEAAAAAAGQEAABjcC9yZTA1L25hbWVzLnB5VVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWPM+sGeCAAAArwAAABYACQAAAAAAAQAAAAAAKAUAAGNwL3JlMDUvdGVtcGVyYXR1cmUucHlVVAUAAQSLKmZQSwECAAAKAAAAAADwlplYAAAAAAAAAAAAAAAACQAJAAAAAAAAABAAAADnBQAAY3AvdGVzdHMvVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWBurfN6OBgAAaSQAABYACQAAAAAAAQAAAAAAFwYAAGNwL3Rlc3RzL3Rlc3RzX3JlMDUucHlVVAUAAQSLKmZQSwECAAAKAAAAAADwlplYAAAAAAAAAAAAAAAAGAAJAAAAAAAAABAAAADiDAAAY3AvdGVzdHMvdW5pdGdyYWRlX2RhdGEvVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWAjPcAFhAAAAcAAAACMACQAAAAAAAAAAAAAAIQ0AAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDEucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWP9MeClgAAAAbgAAACMACQAAAAAAAAAAAAAAzA0AAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDIucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWLOPitlhAAAAcgAAACMACQAAAAAAAAAAAAAAdg4AAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDMucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWGCK6+9eAAAAbQAAACMACQAAAAAAAAAAAAAAIQ8AAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDQucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWK4zA5heAAAAbQAAACMACQAAAAAAAAAAAAAAyQ8AAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDUucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWOhr71lfAAAAbQAAACMACQAAAAAAAAAAAAAAcRAAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDYucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWLxziBpfAAAAbgAAACMACQAAAAAAAAAAAAAAGhEAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDcucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWABkUQFgAAAAbgAAACMACQAAAAAAAAAAAAAAwxEAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDgucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWJYFme9hAAAAcAAAACMACQAAAAAAAAAAAAAAbRIAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMDkucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWKAypqRvAAAAngAAACMACQAAAAAAAAAAAAAAGBMAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMTAucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWJv4eilcAAAAawAAACMACQAAAAAAAAAAAAAA0RMAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMTEucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWO38jKNzAAAAngAAACMACQAAAAAAAAAAAAAAdxQAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMTIucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWMYxv9ByAAAAngAAACMACQAAAAAAAAAAAAAANBUAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMTMucGtsVVQFAAEEiypmUEsBAgAACgAAAAgA8JaZWIb9OU1eAAAAbQAAACMACQAAAAAAAAAAAAAA8BUAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1JlMDVfMTQucGtsVVQFAAEEiypmUEsFBgAAAAAaABoASQgAAJgWAAAoAGEyZDFkYmQxMGE5M2IzMzYyZjQ0MTkyM2VmZGQxNzE4OGRjNTc1NTk=""")