import {ITransferStatus} from './transfer.';

export type IPatient = {
  id: number;
  name: string;
  status: ITransferStatus;
  transferType: ITransferType;
  info: string;
  medicalRecordURL?: string;
  needs?: {
    specialities?: number[];
    hospitalizations?: number[];
  };
};
