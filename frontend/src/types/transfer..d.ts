export type ITransferType = 'local' | 'city' | 'state' | 'country';

export type ITransferStatus =
  | 'emergency'
  | 'veryUrgent'
  | 'urgent'
  | 'lessurgent'
  | 'notUrgent';

export type ITransferTypeText = {
  [key in ITransferType]: string;
};

export type ITransferStatusText = {
  [key in ITransferStatus]: string;
};
