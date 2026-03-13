#!/usr/bin/env python3

import glob
import pathlib

def make_test_sample_set(trigger_text: str) -> None:
    template_dir = pathlib.Path(__file__).parent
    test_dir = pathlib.Path(__file__).parent.parent
    sample_dir = test_dir.joinpath('samples')
    for filename in glob.glob(str(template_dir.joinpath('*-like-*'))):
        template_text = template_dir.joinpath(filename).read_text()
        sample_text = template_text.format(trigger_lower=trigger_text.lower(), trigger_upper=trigger_text.upper(),)
        tmp_path = pathlib.Path(filename)
        sample_filename = f'{tmp_path.stem}-{trigger_text.lower()}{tmp_path.suffix}'
        sample_path = sample_dir.joinpath(sample_filename)
        sample_path.write_text(sample_text)
        print(f'Created {sample_path}')

def main() -> None:
    print('Creating test samples for the following trigger strings:')
    for trigger_text in ['DEBUG', 'FIXME', 'TEST']:
        print(trigger_text)
        make_test_sample_set(trigger_text)
    print('Done')


if __name__ == '__main__':
    main()
