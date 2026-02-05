import json
import click
from pathlib import Path


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help='Output file path (default: input_file with .txt extension)')
@click.option('--skip-no-speaker', is_flag=True, help='Skip entries without speaker information (e.g., music, sound effects)')
def convert(input_file, output, skip_no_speaker):
    """
    Convert ASR JSONL output to plain text format.

    Converts each entry to format: "speaker{N}: {content}"

    Example:
        python scripts/convert_asr_to_txt.py asr_outputs/260117.jsonl
    """
    input_path = Path(input_file)

    # Determine output file path
    if output:
        output_path = Path(output)
    else:
        output_path = input_path.with_suffix('.txt')

    # Read input file
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    # Parse JSON lines
    # The file has header lines, then a JSON array
    lines = content.split('\n')
    json_data = None

    for i, line in enumerate(lines):
        if line.strip().startswith('['):
            # Found the start of JSON array
            json_str = '\n'.join(lines[i:])
            json_data = json.loads(json_str)
            break

    if not json_data:
        click.echo(f"Error: Could not find JSON data in {input_file}", err=True)
        return

    # Convert to text format
    output_lines = []
    for entry in json_data:
        # Skip music and sound effects if requested
        if 'Speaker' not in entry:
            if skip_no_speaker:
                continue
            # Format without speaker
            speaker_label = "[No Speaker]"
        else:
            speaker_num = entry.get('Speaker', 0)
            speaker_label = f"speaker{speaker_num + 1}"  # Convert to 1-indexed

        content_text = entry.get('Content', '')
        output_lines.append(f"{speaker_label}: {content_text}")

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(output_lines))

    click.echo(f"✅ Converted {len(output_lines)} entries")
    click.echo(f"📄 Output saved to: {output_path}")


if __name__ == "__main__":
    convert()
