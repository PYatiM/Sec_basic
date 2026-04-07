def generate_hashes(input_file, output_file, algo='sha256'):
    import hashlib
    with open(input_file, 'r') as f, open(output_file, 'w') as out:
        for line in f:
            word = line.strip().encode()

            if algo == 'md5':
                h = hashlib.md5(word).hexdigest()
            elif algo == 'sha1':
                h = hashlib.sha1(word).hexdigest()
            else:
                h = hashlib.sha256(word).hexdigest()

            out.write(f"{word.decode()}:{h}\n")
