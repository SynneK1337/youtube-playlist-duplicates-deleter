# YouTube Playlist Duplicates Deleter
### **Warning**: It's an ad-hoc tool, so its code is not as quality as it's expected from production-class code. **USE AT YOUR OWN RISK**

## Usage
### Installing dependencies
```shell
pip install -r requirements.txt
```
### Setting up API Credentials
- Go to [Google Developers Console](https://console.developers.google.com/)
- Create a new project
- Navigate to **Library** via a sidebar
- Search for `YouTube Data API v3` and enable it
- Go to **APIs & Services** -> **OAuth consent screen**
- Select **External**, enter whatever **Application name** you like and click **Save**
- On the sidebar, go to **Credentials**
- **CREATE CREDENTIALS** -> **OAuth client ID**
- Select the **Desktop app** and click **Create**
- Click little download icon available in **OAuth 2.0 Client IDs** section **and save the file as `credentials.json` in folder of app**

### Running the script
```
python main.py
```
