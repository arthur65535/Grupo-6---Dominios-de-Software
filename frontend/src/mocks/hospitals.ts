import {IHospital} from '~/types/hospital';

export const hospitals: IHospital[] = [
  {
    name: 'Hospital das Clínicas da UFG',
    city: 'Goiânia',
    state: 'Goiás',
    country: 'Brasil',
    phone: '+556232047100',
    geolocation: {
      latitude: -16.6745663,
      longitude: -49.2449164,
    },
    specialities: [0, 16, 19, 33],
    hospitalizations: [12, 14, 20],
  },

  {
    name: 'Hospital Israelita Albert Einstein',
    city: 'São Paulo',
    state: 'São Paulo',
    country: 'Brasil',
    phone: '+551133820374',
    geolocation: {
      latitude: -34.5850669,
      longitude: -58.4016626,
    },
    specialities: [0, 1, 4, 34, 35, 36],
    hospitalizations: [1, 2, 7, 8, 9, 20],
  },

  {
    name: 'Hospital General de Agudos B. Rivadavia',
    city: 'Buenos Aires',
    country: 'Argentina',
    phone: '+541148092000',
    geolocation: {
      latitude: -16.6962644,
      longitude: -49.2695843,
    },
    specialities: [0, 1, 3, 4, 5, 7, 21, 34, 35, 36, 48],
    hospitalizations: [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 20],
  },
];
