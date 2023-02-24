import React, {useState} from 'react';

// Routes
import AppRoutes from '~/routes/app.routes';
import Login from '~/screens/Login';

const Routes: React.FC = () => {
  const [login, setLogin] = useState(false);

  if (!login) {
    return <Login onPress={() => setLogin(true)} />;
  }

  return <AppRoutes />;
};

export default Routes;
