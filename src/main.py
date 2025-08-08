import typer  # Import the Typer library for building CLI applications

app = typer.Typer()  # Create a Typer app instance

@app.command()  # Register the following function as a CLI command
def hello(greet):  # Define the 'hello' command function
    """Say hello to DevHelper AI"""  # Docstring describing the command
    typer.echo("👋 Hello from DevHelper AI!")  # Print a greeting message to the console

if __name__ == "__main__":  # Check if this script is being run directly
    app()  # Run the Typer CLI