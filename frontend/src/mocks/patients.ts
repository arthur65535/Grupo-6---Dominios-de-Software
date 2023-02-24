import {IPatient} from '~/types/patient';

const patients: IPatient[] = [
  {
    id: 0,
    name: 'João da Silva',
    status: 'emergency',
    transferType: 'local',
    info: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temp incididunt ut labore et dolore magna aliqua. Magnaetiam tempor orci eu lobort elementum. Risus sed vulputate odiout. In ante metus dictum at tempor commo ullamcorper a lacus. Tempus egestas sed sed risus. Vestibulum rhoncus est pellentesque elit. Ultricies integer quis auctor elit sed. Curabitur gravida arcu ac tortor dignissim convallis. Massa tempor nec feugiat nisl pretium. In ante metus dictum at tempor commodo ullamcorper a lacus. Urna id volutpat lacus laoreet. Quam lacus suspendisse faucibus interdum posuere. At in tellus integer feugiat scelerisque varius. Pulvinar neque laoreet suspendisse interdum. Ultricies mi quis hendrerit dolor.',
    medicalRecordURL: 'https://www.africau.edu/images/default/sample.pdf',
    needs: {
      specialities: [0],
      hospitalizations: [14],
    },
  },
  {
    id: 1,
    name: 'Lucas da Silva Santos',
    status: 'veryUrgent',
    transferType: 'state',
    info: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temp incididunt ut labore et dolore magna aliqua. Magnaetiam tempor orci eu lobort elementum. Risus sed vulputate odiout. In ante metus dictum at tempor commo ullamcorper a lacus. Tempus egestas sed sed risus. Vestibulum rhoncus est pellentesque elit. Ultricies integer quis auctor elit sed. Curabitur gravida arcu ac tortor dignissim convallis. Massa tempor nec feugiat nisl pretium. In ante metus dictum at tempor commodo ullamcorper a lacus. Urna id volutpat lacus laoreet. Quam lacus suspendisse faucibus interdum posuere. At in tellus integer feugiat scelerisque varius. Pulvinar neque laoreet suspendisse interdum. Ultricies mi quis hendrerit dolor.',
    medicalRecordURL: 'https://www.africau.edu/images/default/sample.pdf',
    needs: {
      hospitalizations: [20],
    },
  },
  {
    id: 2,
    name: 'Bruno Leonardo Dias Antunes',
    status: 'urgent',
    transferType: 'country',
    info: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temp incididunt ut labore et dolore magna aliqua. Magnaetiam tempor orci eu lobort elementum. Risus sed vulputate odiout. In ante metus dictum at tempor commo ullamcorper a lacus. Tempus egestas sed sed risus. Vestibulum rhoncus est pellentesque elit. Ultricies integer quis auctor elit sed. Curabitur gravida arcu ac tortor dignissim convallis. Massa tempor nec feugiat nisl pretium. In ante metus dictum at tempor commodo ullamcorper a lacus. Urna id volutpat lacus laoreet. Quam lacus suspendisse faucibus interdum posuere. At in tellus integer feugiat scelerisque varius. Pulvinar neque laoreet suspendisse interdum. Ultricies mi quis hendrerit dolor.',
    medicalRecordURL: 'https://www.africau.edu/images/default/sample.pdf',
    needs: {
      hospitalizations: [1],
    },
  },
  {
    id: 3,
    name: 'Luiz Candido Medeiros',
    status: 'notUrgent',
    transferType: 'city',
    info: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temp incididunt ut labore et dolore magna aliqua. Magnaetiam tempor orci eu lobort elementum. Risus sed vulputate odiout. In ante metus dictum at tempor commo ullamcorper a lacus. Tempus egestas sed sed risus. Vestibulum rhoncus est pellentesque elit. Ultricies integer quis auctor elit sed. Curabitur gravida arcu ac tortor dignissim convallis. Massa tempor nec feugiat nisl pretium. In ante metus dictum at tempor commodo ullamcorper a lacus. Urna id volutpat lacus laoreet. Quam lacus suspendisse faucibus interdum posuere. At in tellus integer feugiat scelerisque varius. Pulvinar neque laoreet suspendisse interdum. Ultricies mi quis hendrerit dolor.',
    needs: {
      specialities: [16],
      hospitalizations: [],
    },
  },
];

export default patients;
