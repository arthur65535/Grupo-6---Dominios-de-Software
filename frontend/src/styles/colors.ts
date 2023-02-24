import {ITransferStatus} from '~/types/transfer.';

const colors = {
  primary: '#3A4D6E',
  secondary: '#E0A100',
  tertiary: '#182539',

  info: '#0077E5',
  success: '#00E417',
  warning: '#DAC400',
  danger: '#B20000',

  white: '#FFFFFF',
  black: '#000000',
  ice: '#CECECE',
  grey: '#AAAAAA',
};

const statusColor: {[key in ITransferStatus]: string} = {
  emergency: '#B20000',
  veryUrgent: '#E0A100',
  urgent: '#DAC400',
  lessurgent: '#00E417',
  notUrgent: '#0077E5',
};

export default colors;

export {statusColor};
