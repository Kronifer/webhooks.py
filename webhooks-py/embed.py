from typing import Optional

class Embed:
    """
    A class for discord embeds.
    Params:
        title: A string representing the embed title.
        description: An optional string representing the description.
        color: An optional string containing the hex code of a color.
        
    Functions:
        add_field:
            Params:
                name: A string representing the field's title.
                value: A string representing the field's content.
                inline: An optional boolean indicating whether or not the field is inline.
        set_footer:
            Params:
                text: A string representing the footer of the embed.
    """
    def __init__(
        self,
        title: str,
        description: Optional[str],
        color: Optional[str]
    ):
        self.title = title
        self.description = description
        self.color = color
        self.fields = []
        self.footer: str = None
    
    def add_field(self, name: str, value: str, inline: Optional[bool]):
        self.fields.append(
            {
                "name": name,
                "value": value,
                "inline": inline if inline else False
            }
        )

    def set_footer(self, text: str):
        self.footer = text

    def _to_json(self):
        json = {}
        json.update(
            {
                "title": self.title,
                "type": "rich",
            }
        )
        if self.description is not None:
            json.update({"description": self.description})
        if self.color is not None:
            json.update({"color": int(self.color, 16)})
        if self.fields != []:
            json.update({"fields": self.fields})
        if self.footer is not None:
            json.update({"footer": self.footer})
        return json