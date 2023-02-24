import React, {useState} from 'react';
import {Event} from 'react-native';

// Libs
import {RouteProp, useRoute} from '@react-navigation/native';
import PDFViewer from 'react-native-pdf';

// Types
import {RootStackParamList} from '~/routes/app.routes';

// Styles
import {Container} from './styles';

const PDF: React.FC = () => {
  const route = useRoute<RouteProp<RootStackParamList, 'PDF'>>();

  const [PDFViewDimensions, setPDFViewDimensions] = useState({
    width: 0,
    height: 0,
  });

  const source = {
    uri: route.params.uri,
    cache: true,
  };

  return (
    <Container
      onLayout={(event: Event) => {
        const {width, height} = event.nativeEvent.layout;
        setPDFViewDimensions({width, height});
      }}>
      <PDFViewer
        source={source}
        onLoadComplete={numberOfPages => {
          console.log(`Number of pages: ${numberOfPages}`);
        }}
        onPageChanged={page => {
          console.log(`Current page: ${page}`);
        }}
        onError={error => {
          console.log(error);
        }}
        onPressLink={uri => {
          console.log(`Link pressed: ${uri}`);
        }}
        style={{
          width: PDFViewDimensions.width,
          height: PDFViewDimensions.height,
        }}
      />
    </Container>
  );
};

export default PDF;
