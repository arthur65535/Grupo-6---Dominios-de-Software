import {IGeolocation} from './geolocation';

export type IHospital = {
  name: string;
  city: string;
  state?: string;
  country: string;
  phone: string;
  geolocation: IGeolocation;
  specialities: number[];
  hospitalizations: number[];
};
