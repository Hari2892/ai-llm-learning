import os
import requests
import argparse
from dotenv import load_dotenv
import sys

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY") # Make sure to set this in your .env file
API_URL = "https://api.openai.com/v1/responses" # Updated to the correct endpoint for responses

def call_llm(prompt, model="gpt-4.1-mini", temperature=0.7):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "input": prompt,
        "temperature": temperature
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/responses",
            headers=headers,
            json=data,
            timeout=30
        )

        try:
            resp_json = response.json()
        except ValueError:
            return {
                "success": False,
                "status": response.status_code,
                "error": response.text,
                "code": "invalid_json"
            }

        if response.status_code != 200:
            message = resp_json.get("error", {}).get("message", "Unknown error")
            code = resp_json.get("error", {}).get("code", "no_code")

            return {
                "success": False,
                "status": response.status_code,
                "error": message,
                "code": code
            }

        try:
            content = resp_json["output"][0]["content"][0]["text"]
        except (KeyError, IndexError):
            return {
                "success": False,
                "status": "parse_error",
                "error": f"Unexpected response format: {resp_json}",
                "code": "parse_error"
            }

        return {
            "success": True,
            "data": content
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "status": "network_error",
            "error": str(e),
            "code": "network_error"
        }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=30) # Added timeout for better error handling

        # Try parsing JSON safely
        try:
            resp_json = response.json()
        except ValueError:
            return {
                "success": False,
                "status": response.status_code,
                "error": response.text,
                "code": "invalid_json"
            }

        # ✅ Handle API errors properly
        if response.status_code != 200:
            message = resp_json.get("error", {}).get("message", "Unknown error")
            code = resp_json.get("error", {}).get("code", "no_code")

            return {
                "success": False,
                "status": response.status_code,
                "error": message,
                "code": code
            }

        # ✅ Handle success response
        try:
            content = resp_json["choices"][0]["message"]["content"] # This is the expected path for a successful response
        except (KeyError, IndexError):
            return {
                "success": False,
                "status": "parse_error",
                "error": f"Unexpected response format: {resp_json}",
                "code": "parse_error"
            }

        return {
            "success": True,
            "data": content
        }

    except requests.exceptions.RequestException as e: # Catching all request-related exceptions
        return {
            "success": False,
            "status": "network_error",
            "error": str(e),
            "code": "network_error"
        }


def main():
    parser = argparse.ArgumentParser(description="Simple LLM CLI tool") # Added description for better help message
    parser.add_argument("prompt", type=str, help="Prompt to send to LLM")
    parser.add_argument("--model", default="gpt-4.1-mini") # Default model is set to gpt-4.1-mini, but can be overridden with --model flag
    parser.add_argument("--temperature", type=float, default=0.7)

    args = parser.parse_args()

    result = call_llm(args.prompt, args.model, args.temperature) # Passing model and temperature from command line arguments

    if result["success"]:
        print("\n🤖 Response:\n")
        print(result["data"])
    else:
        print("\n❌ Error:")
        print(f"Status: {result['status']}")
        print(f"Code: {result['code']}")
        print(f"Message: {result['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()