import os
import sys
import time
import webbrowser

print('__file__: %s' % __file__)
path1 = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path1)
base_path = os.path.dirname(path1)
sys.path.append(base_path)
os.environ['PYTHONPATH'] = path1
print('path1', path1, flush=True)

os.environ['NLTK_DATA'] = os.path.join(base_path, './nltk_data')
os.environ['PATH'] = os.environ['PATH'] + ';' + \
                     os.path.join(base_path, 'poppler/Library/bin/') + ';' + \
                     os.path.join(base_path, 'poppler/Library/lib/') + ';' + \
                     os.path.join(base_path, 'Tesseract-OCR')
print(os.environ['PATH'])

for sub in ['src', 'iterators', 'gradio_utils', 'metrics', 'models', '.']:
    path2 = os.path.join(base_path, '..', sub)
    sys.path.append(path2)
    print(path2, flush=True)

    path2 = os.path.join(path1, '..', sub)
    sys.path.append(path2)
    print(path2, flush=True)


def main():
    from gen import main as main_h2ogpt
    main_h2ogpt(block_gradio_exit=False, score_model=None)

    url = "http://localhost:%s" % os.getenv('GRADIO_SERVER_PORT', str(7860))
    webbrowser.open(url)

    while True:
        time.sleep(10000)


if __name__ == "__main__":
    main()
