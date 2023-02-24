import {ITransferStatus, ITransferType} from '~/types/transfer.';

export const TRANSFER_TYPE: {[key in ITransferType]: string} = {
  local: 'Transferência Local',
  city: 'Transferência Municipal',
  state: 'Transferência Estadual',
  country: 'Transferência Internacional',
};

export const TRANSFER_STATUS: {[key in ITransferStatus]: string} = {
  emergency: 'Emergência',
  veryUrgent: 'Muito urgente',
  urgent: 'Urgente',
  lessurgent: 'Pouco urgente',
  notUrgent: 'Não urgente',
};
