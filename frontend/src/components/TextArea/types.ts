import {TextInputProps} from 'react-native';

export interface ITextArea extends TextInputProps {
  value: string;
  errorMessage?: string;
}

export interface ITextAreaViewModel {
  value: string;
}
