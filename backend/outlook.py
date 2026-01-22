import markdown

def generate_outlook(exchange, inflation):
    text = f"""
# Nigeria Economic Outlook

## Inflation
Inflation is currently around **{inflation}%**, remaining elevated.

## Exchange Rate
USD/NGN trades near **{exchange}**, reflecting FX pressure.

## Outlook
Monetary conditions are expected to remain tight.
"""
    return markdown.markdown(text)
