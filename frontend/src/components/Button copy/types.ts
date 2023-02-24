import {ButtonProps} from 'react-native';

export interface IButton extends ButtonProps {
  title: string;
  onPress?: () => void;
  loading?: boolean;
  color?: string;
  background?: string;
}

export interface IButtonViewModel {
  onPress?: () => void;
  loading?: boolean;
}
