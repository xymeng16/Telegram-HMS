## Telegram Cilent for Android with Huawei Mobile Services Push Kit support

A customized Telegram client and relay server that can receive HMS Push Notification on Huawei Devices. This client allows Huawei users to receive Telegram messages without keeping the client alive at the background, eliminating the possible message missing incidence due to the battery policy of EMUI/HarmonyOS.

### How to use
#### Client
1. [**Obtain your own api_id**](https://core.telegram.org/api/obtaining_api_id) for your application.
2. Replace the corresponding information (APP_ID, APP_HASH, etc.) in TMessagesProj/src/main/java/org/telegram/hmsmsger/BuildVArs.java
3. Replace the original package name org.telegram.hmsmsger with your customized one (This step is essential since the package name must be unique at next step)
4. Register as a Huawei Developer, and create a new project then a new APP using your own package name in the AppConnect Console. Enable Push Kit and download the corresponding agconnect-service.json file to replace the dummy one under TMessagesProj/ directory. Make sure to add the given code inside the correct build.gradle files. For more detail of this step, please refer to the official tutorial of Huawei.
5. Follow the official tutorial of Google Firebase to create APP and integrate Firebase into your APP. Remember to replace the dummy google-services.json under TMessagesProj/ directory with your own one and add the given code inside the correct build.gradle files.
6. Use any approach you like to acquire the HMS PushToken of your Huawei Device. In this client I have implemented one possible approach in the ApplicationLoader.java file, named getToken(), FYR. 
7. Choose a proper build variant and then build the project and test it on your Huawei Device.
#### Relay Server
The relay server is written with Python, and some code are copied from [hms-push-serverdemo-python](https://github.com/HMS-Core/hms-push-serverdemo-python/tree/master/python37). Its design rationale is receiving the incoming message via the MTProto API of Telegram then pushing the message to your Huawei Phone. Here I use [Telethon](https://github.com/LonamiWebs/Telethon) to implement above operations.  
In order to run the server, please follow these steps:
1. Install Telethon and any required dependencies using your package management tools.
2. Open telepy/tele.py replace [api_id, api_hash] (for Telegram) and [app_id, app_secret] (for HMS) with your own values. Make sure to run this program on a trusted server since the leakage of that information may incur the loss of your privacy and properties.
3. Run the tele.py and log in with your Telegram account. Login is only required the first time you run the server program. 
4. Keep it running in the background via nohup/screen or any tools you like.
5. Try if you can receive push notification on your Huawei Device! If not, you may check the output to see what happened.
