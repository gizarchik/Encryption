import parser
import decode
import encode
import hack
import training


def main():
    arguments = parser.parse()

    if arguments['type'] == 'encode' or arguments['type'] == 'decode':
        try:
            input_file = open(arguments['input_file'])
        except Exception:
            raise Exception

        try:
            output_file = open(arguments['output_file'], 'a')
        except Exception:
            input_file.close()
            raise Exception

        if arguments['cipher'] == 'caesar':
            try:
                key = int(arguments['key'])
            except Exception:
                input_file.close()
                output_file.close()
                raise Exception
            if key < 0 or key >= 26:
                input_file.close()
                output_file.close()
                raise ValueError('Wrong key')
            else:
                if arguments['type'] == 'encode':
                    encode.encode_caesar(key, input_file, output_file)
                else:
                    decode.decode_caesar(key, input_file, output_file)
        elif arguments['cipher'] == 'vigenere':
            try:
                key = arguments['key']
                key = key.lower()
            except Exception:
                input_file.close()
                output_file.close()
                raise Exception

            if arguments['type'] == 'encode':
                encode.encode_vigener(key, input_file, output_file)
            else:
                decode.decode_vigener(key, input_file, output_file)

        elif arguments['cipher'] == 'vernam':
            try:
                key_file = open(arguments['key'])
            except Exception:
                raise Exception
            try:
                if arguments['type'] == 'encode':
                    encode.encode_vernam(key_file, input_file, output_file)
                else:
                    decode.decode_vernam(key_file, input_file, output_file)
            except:
                raise ValueError('Key is wrong')
        else:
            raise ValueError('Unknown cipher, use caesar, vigenere or vernam')
    elif arguments['type'] == 'training':
        try:
            input_file = open(arguments['input_file'], encoding='ISO-8859-5')
        except Exception:
            raise Exception

        try:
            output_file = open(arguments['output_file'], 'a')
        except Exception:
            input_file.close()
            raise Exception

        if arguments['cipher'] == 'caesar':
            training.training_caesar(input_file, output_file)
    elif arguments['type'] == 'hack':
        try:
            analysis_file = open(arguments['frequency_analysis_file'])
        except Exception:
            raise Exception
        try:
            input_file = open(arguments['input_file'])
        except Exception:
            analysis_file.close()
            raise Exception

        try:
            output_file = open(arguments['output_file'], 'a')
        except Exception:
            input_file.close()
            analysis_file.close()
            raise Exception

        if arguments['cipher'] == 'caesar':
            try:
                hack.hack_caesar(analysis_file, input_file, output_file, arguments['input_file'])
            except Exception:
                raise Exception


if __name__ == '__main__':
    main()
