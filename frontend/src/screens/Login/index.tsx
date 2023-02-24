import React, {useState} from 'react';
import Button from '~/components/Button';
import TextInput from '~/components/TextInput';

// Styles
import {Container, BackgrounImage, Content} from './styles';

const Template: React.FC<{onPress: () => void}> = ({onPress}) => {
  const [email, setEmail] = useState('');
  const [pass, setPass] = useState('');
  return (
    <Container>
      <BackgrounImage />
      {/* <Icon SVG={Logo} size={100} /> */}
      <Content>
        <TextInput
          placeholder="Email"
          value={email}
          onChangeText={value => setEmail(value)}
        />

        <TextInput
          placeholder="Senha"
          value={pass}
          onChangeText={value => setPass(value)}
          secureTextEntry
        />

        <Button
          title="Entrar"
          onPress={onPress}
          // loading
        />
      </Content>
    </Container>
  );
};

export default Template;
