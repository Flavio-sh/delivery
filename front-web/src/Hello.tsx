type Props = {
    message: string;
}

export default function Hello({ message }: Props) {

    return (
        <h1>Componente {message}!</h1>
    )
}

