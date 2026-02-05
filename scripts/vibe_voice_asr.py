from gradio_client import Client, handle_file
import click


@click.command()
@click.argument('audio_file', type=click.Path(exists=True))
def transcribe(audio_file):
    with open('./docs/术语表.md', 'r') as f:
        context_info = f.read().strip()

    client = Client("https://4e47b675ea4015a607.gradio.live/")
    result = client.predict(
        file_input=handle_file(audio_file),
        audio_rec=None,
        video_rec=None,
        audio_prev=handle_file(audio_file),
        video_prev=None,
        max_tokens=32768,
        temp=0,
        top_p=1,
        do_sample=False,
        context_info=context_info,
        api_name="/transcribe_wrapper"
    )
    print(result)


if __name__ == "__main__":
    transcribe()