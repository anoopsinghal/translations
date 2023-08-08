/** @format */

import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View, TextInput, Button, Alert } from "react-native";

const LanguageTranslation = (props) => {
  return (
    <View style={{padding:10}}>
      <Text>{props.prompt}</Text>
      <TextInput
        style={{
          height: 40,
          borderColor: 'gray',
          borderWidth: 1,
        }}
      />
    </View>    
  );
};

export default function App() {
  return (
    <View style={styles.container}>
      <LanguageTranslation prompt='English text to translate'/>
      <Button
        title="Translate text"
        color="blue"
        onPress={() => Alert.alert('Simple Button pressed')}
      />      
      <LanguageTranslation prompt='Translated French text'/>
      <LanguageTranslation prompt='Translated German text'/>
      <LanguageTranslation prompt='Translated Spanish text'/>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "left",
    justifyContent: "center",
    padding:10,
  },
  textarea: {
    borderBottomColor: "#000000",
    borderBottomWidth: 1,
    padding: 10,
    width:'1000',
  },
});
