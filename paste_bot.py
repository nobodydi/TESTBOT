import requests

def create_pastebin_paste(api_key, text, visibility='private', expiration='1D'):
    data = {
        'api_dev_key': api_key,
        'api_paste_data': text,
        'api_paste_private': '1' if visibility == 'private' else '0',
        'api_paste_expire_date': expiration
    }

    response = requests.post('https://pastebin.com/api/api_post.php', data=data)

    if response.ok:
        paste_url = response.text
        return paste_url
    else:
        return None

if __name__ == "__main__":
    # Replace 'your_pastebin_api_key' with your actual Pastebin API key
    pastebin_api_key = 'your_pastebin_api_key'

    # Example text to be pasted
    example_text = "Hello, this is a test paste!"

    # Create a private paste that expires in 1 day
    paste_url = create_pastebin_paste(pastebin_api_key, example_text, visibility='private', expiration='1D')

    if paste_url:
        print(f"Pastebin URL: {paste_url}")
    else:
        print("Error creating Pastebin paste. Please check your API key and try again.")
