sampleData = [
  {
    "id": "msg_67b73f697ba4819183a15cc17d011509",
    "type": "message",
    "role": "assistant",
    "content": [
      {
        "type": "output_text",
        "text": "Under the soft glow of the moon, Luna the unicorn danced through fields of twinkling stardust, leaving trails of dreams for every child asleep.",
        "annotations": []
      }
    ]
  }
]

#print(f"Message ID: {sampleData[0]['id']}\n")  # Accessing the 'id' of the first dictionary in the list
print(f"content: {sampleData[0]['content'][0]['text']}") # Accessing the 'text' of the first content dictionary in the list