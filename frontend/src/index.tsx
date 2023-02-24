import React from 'react';
import {LogBox} from 'react-native';

import Routes from './routes';

const STP: React.FC = ({}) => {
  LogBox.ignoreAllLogs();
  return <Routes />;
};

export default STP;
