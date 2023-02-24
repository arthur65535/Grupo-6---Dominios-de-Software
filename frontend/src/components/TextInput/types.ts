import {TextInputProps} from 'react-native';

export interface ITextInput extends TextInputProps {
  value: string;
  mask?: Array<string | RegExp>;
  errorMessage?: string;
}

export interface ITextInputViewModel {
  value: string;
}
