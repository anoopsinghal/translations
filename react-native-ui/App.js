/** @format */
import React, { useState } from "react";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, View, TextInput, Button, Alert } from "react-native";
import { TRANSLATION_SERVER_API_URL } from "@env"

function LanguageTranslation({ label, prompt, onChangeTextFn }) {
  return (
    <View style={{ padding: 10 }}>
      <TextInput
        style={{
          height: 40,
          borderColor: "gray",
          borderWidth: 1,
          padding: 10,
          width: 300,
        }}
        onChangeText={onChangeTextFn}
        placeholder={label}
      >
        {prompt}
      </TextInput>
    </View>
  );
}

Translate = async (fromLang, fromStr, toLang, toStrFn) => {
  try {
    let response = await fetch(TRANSLATION_SERVER_API_URL, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({
        fromLang: fromLang,
        fromStr: fromStr,
        toLang: toLang,
      }),
    });
    let responseJson = await response.json();
    console.log(responseJson);
    toStrFn(responseJson["toStr"]);
  } catch (error) {
    console.error(error);
  }
};

export default function App() {
  const [englishText, setEnglishText] = useState("");
  const [frenchText, setFrenchText] = useState("");
  const [germanText, setGermanText] = useState("");
  const [spanishText, setSpanishText] = useState("");

  return (
    <View style={styles.container}>
      <LanguageTranslation
        label="English text to translate"
        prompt={englishText}
        onChangeTextFn={(newText) => setEnglishText(newText)}
      />
      <Button
        title="Translate text"
        color="blue"
        onPress={() => {
          Translate("en", englishText, "fr", setFrenchText);
          Translate("en", englishText, "de", setGermanText);
          Translate("en", englishText, "es", setSpanishText);
        }}
      />
      <LanguageTranslation label="Translated French text" prompt={frenchText} />
      <LanguageTranslation label="Translated German text" prompt={germanText} />
      <LanguageTranslation
        label="Translated Spanish text"
        prompt={spanishText}
      />
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
    padding: 10,
  },
  textarea: {
    borderBottomColor: "#000000",
    borderBottomWidth: 1,
    padding: 10,
    width: "1000",
  },
});
