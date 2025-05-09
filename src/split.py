def get_bucket_from_full_path(uri: str) -> str:
    return uri.split("/")[2]


uri = "gs://my-bucket/path/to/file.txt"
bucket = get_bucket_from_full_path(uri)
print(bucket)

uri = "gs://my-bucket/path/to/file.txt"
bucket = get_bucket_from_full_path(uri)
print(bucket)
