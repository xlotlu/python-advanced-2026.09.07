# Scrieți o funcție `cp(source, target)`
# ce copiază fișierul cu cale `source` în `target`

def cp(source, target, chunk_size=4096):
    with open(source, 'br') as f_in, \
         open(target, 'bw') as f_out:

        # introducing... the "walrus" operator
        while content := f_in.read(chunk_size):
            f_out.write(content)
