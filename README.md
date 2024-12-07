# vnr-campus-navigator

## How to start 

```
git clone git@github.com:Vignana-Jyothi/vnr-campus-navigator.git
```

### Using Android Studio
Open using Android studio (wait for the Gradle to build the project)
Run the app using ```Shift + F10```

### Using command line  (in linux)

```
./gradlew build
./gradlew assembleDebug
```
This generates .apk file that you can transfer & install on your phone. 

**Note**: this is small prototype to showcase idea. It has huge room for improvement.  All the best in automating VNR Campus Navigation. 
*Need more help??* More detailed instructions to run in linux or Windows can be found at the bottom of this page. 


## Approach
**Annotations**
- [room_cards_tagger.py](https://github.com/Vignana-Jyothi/vnr-campus-navigator/blob/main/annotation_tool/room_cards_tagger.py) Use  DrawRectangle with Control key to genrate rectangle coordinates. - 
- appsrc/main/../MainActivity : Loads the room numbers & handles clicks & item selection
- HighlightView.kt :
  - Contains the map details for each room.
  - Handles Drawing & all business logic. 


**Not yet launched**
- render.py : Loads college A-Block 2nd floor image & shows the tagged rooms.
- [render.py](https://github.com/Vignana-Jyothi/vnr-campus-navigator/blob/main/annotation_tool/render.py) is used to draw rectangle on image & identify coordinates.
- [room_detection.py](https://github.com/Vignana-Jyothi/vnr-campus-navigator/blob/main/annotation_tool/room_cards_tagger.py), custom_room_selector.py Detects room automatically. But not perfected yet. 
 

## How to use the app

### Using Spinner (Dropdown)
Select a Room you want to go to. See it getting highlighted. 


Change to different room by selecting it. 

| Show Room    | Change Room |
| -------- | ------- |
| ![image](https://github.com/user-attachments/assets/1efd688c-70bc-45ca-a843-d60f8a1418ea)  | ![image](https://github.com/user-attachments/assets/01749143-d321-4830-bf29-273811e8a334)   |


### Using Click/Tapping
Click any room. It selects the room automatically. 
![image](https://github.com/user-attachments/assets/5cd06ae1-2a19-4eb2-baa6-92e57b3d4ec1)

Note: Only Few rooms are annotated. Other rooms may not work. 


# Detailed Steps in Ubuntu (linux OS)

### **1. Prerequisites**
Ensure you have the following installed:
- **JDK**: Java Development Kit (version 11 or above is typically required for Android projects).
- **Android SDK**: Ensure Android Studio or the command-line tools are installed, and the `ANDROID_HOME` environment variable is configured.
- **Gradle**: Install Gradle or use the Gradle wrapper (`gradlew`) included in the project.

---

### **2. Clone the Repository**
Clone the project to your local machine:

```bash
git clone https://github.com/Vignana-Jyothi/vnr-campus-navigator.git
cd vnr-campus-navigator/android/app
```

---

### **3. Check Gradle Wrapper**
Ensure the project has a Gradle wrapper (`gradlew` and `gradlew.bat`) in the root directory or the `android/app` folder. If it exists, you don’t need to install Gradle manually.

- Make the wrapper executable (on Linux/macOS):
  ```bash
  chmod +x ./gradlew
  ```

---

### **4. Sync Dependencies**
Download the necessary dependencies for the project:

```bash
./gradlew build
```

This will fetch all required dependencies and compile the project.

---

### **5. Build the APK**
To build the APK file:

```bash
./gradlew assembleDebug
```

- The APK file will be generated in the following directory:
  ```
  android/app/build/outputs/apk/debug/
  ```

For a release build:
```bash
./gradlew assembleRelease
```

---

### **6. Run the Application**
If you want to install and run the application on a connected Android device or emulator:
1. **Ensure a Device is Connected**:
   - Use `adb devices` to confirm your device is listed.

2. **Run the App**:
   ```bash
   ./gradlew installDebug
   ```

   This installs the app on the connected device.

3. **Launch the App**:
   ```bash
   adb shell am start -n com.vnr.campusnavigator/.MainActivity
   ```

   Replace `com.vnr.campusnavigator` with the correct package name from the project if different.

---

### **7. Troubleshooting**
- **Android SDK Not Found**:
  - Ensure the `ANDROID_HOME` environment variable is set and points to the Android SDK directory.

  Example (Linux/macOS):
  ```bash
  export ANDROID_HOME=/path/to/android-sdk
  export PATH=$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH
  ```

- **Dependencies Missing**:
  - Ensure that all dependencies in the `build.gradle.kts` file are correctly synced.

---
# Detailed Steps in Windows OS
Here’s how to run the project **VNR Campus Navigator** using **Gradle** on a Windows system:

---

### **1. Prerequisites**
Make sure you have the following installed on your Windows machine:

1. **Java Development Kit (JDK)**:
   - Download and install the JDK (11 or above) from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html) or [OpenJDK](https://openjdk.org/).
   - Add the `JAVA_HOME` environment variable:
     - Go to **System Properties > Advanced > Environment Variables**.
     - Add `JAVA_HOME` pointing to your JDK installation directory (e.g., `C:\Program Files\Java\jdk-17`).
     - Add `%JAVA_HOME%\bin` to your **Path**.

   Verify installation:
   ```cmd
   java -version
   ```

2. **Android SDK**:
   - Install Android Studio or [Command Line Tools](https://developer.android.com/studio#downloads).
   - Configure `ANDROID_HOME`:
     - Set `ANDROID_HOME` to the location of the Android SDK (e.g., `C:\Users\<YourUser>\AppData\Local\Android\Sdk`).
     - Add `%ANDROID_HOME%\platform-tools` and `%ANDROID_HOME%\tools` to your **Path**.

   Verify installation:
   ```cmd
   adb --version
   ```

3. **Gradle (Optional)**:
   - The project includes a Gradle wrapper (`gradlew`), so you don’t need to install Gradle manually. However, if you'd like to install Gradle globally, you can download it from [Gradle.org](https://gradle.org/releases/).

---

### **2. Clone the Repository**
1. Open a terminal (e.g., Command Prompt or PowerShell).
2. Clone the GitHub repository:
   ```cmd
   git clone https://github.com/Vignana-Jyothi/vnr-campus-navigator.git
   cd vnr-campus-navigator\android\app
   ```

---

### **3. Run Gradle Commands**
The project includes the Gradle wrapper (`gradlew.bat`), which allows you to run Gradle commands without installing Gradle globally.

#### **Step 1: Sync Dependencies**
To download and sync all required dependencies:
```cmd
gradlew.bat build
```

#### **Step 2: Build the APK**
To build the debug APK:
```cmd
gradlew.bat assembleDebug
```

- The APK file will be located in:
  ```
  vnr-campus-navigator\android\app\build\outputs\apk\debug\app-debug.apk
  ```

For a release APK:
```cmd
gradlew.bat assembleRelease
```

---

### **4. Install and Run the App**
1. Connect your Android device via USB or start an emulator:
   - Use the `adb` command to confirm a connected device:
     ```cmd
     adb devices
     ```

2. Install the APK on the connected device:
   ```cmd
   adb install .\build\outputs\apk\debug\app-debug.apk
   ```

3. Launch the app:
   ```cmd
   adb shell am start -n com.vnr.campusnavigator/.MainActivity
   ```

Replace `com.vnr.campusnavigator` with the correct package name if it’s different.

---

### **5. Troubleshooting on Windows**
- **Environment Variables Not Set**:
   - Ensure `JAVA_HOME` and `ANDROID_HOME` are correctly configured under **System Properties > Advanced > Environment Variables**.
   - Verify with:
     ```cmd
     echo %JAVA_HOME%
     echo %ANDROID_HOME%
     ```

- **Gradle Errors**:
   - If `gradlew.bat` fails, delete the `.gradle` folder in the project directory and re-run:
     ```cmd
     del .gradle /S /Q
     gradlew.bat clean build
     ```

- **SDK Version Errors**:
   - Open `build.gradle.kts` and ensure the `compileSdkVersion` matches the installed SDK version in your Android SDK.

---

With these steps, you should be able to build and run the project on your Windows system. Let me know if you need further assistance! 😊
