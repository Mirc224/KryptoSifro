import requests, zipfile, io
# def download_url(url, save_path, chunk_size=128):
#     r = requests.get(url, stream=True)
#     with open(save_path, 'wb') as fd:
#         for chunk in r.iter_content(chunk_size=chunk_size):
#             fd.write(chunk)

# for i in range(50, 51):
#     zip_file_url = f'http://www.utm.edu/~caldwell/primes/millions/primes{i}.zip'
#     r = requests.get(zip_file_url, stream=True)
#     z = zipfile.ZipFile(io.BytesIO(r.content))
#     z.extractall(f'Primes/')

result = []

for i in range(1, 51):
    with open('Primes/primes1.txt') as f:
        lines = f.readlines()
        del lines[0]
        del lines[0]
        for line in lines:
            tmp = line.split()
            result.extend(tmp)
with open('Primes/all_primes.txt', 'w') as f:
    f.writelines('\n'.join(result))