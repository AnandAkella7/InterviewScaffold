import { ApolloClient, InMemoryCache, ApolloProvider, gql, useQuery, useMutation } from '@apollo/client';
import { useState } from 'react';
import './App.css'; // Optional additional styles

// --- APOLLO CLIENT SETUP ---
const client = new ApolloClient({
    uri: 'http://localhost:8000/graphql',
    cache: new InMemoryCache(),
});

// --- GRAPHQL OPERATIONS ---
// Define your queries and mutations here
const HELLO_QUERY = gql`
  query GetHello {
    hello
  }
`;

// Example mutation
// const CREATE_USER = gql`
//   mutation CreateUser($name: String!) {
//     createUser(name: $name) {
//       name
//     }
//   }
// `;

function Content() {
    const { loading, error, data } = useQuery(HELLO_QUERY);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}</p>;

    return (
        <div>
            <h1>Interview Scaffold</h1>
            <div className="card">
                <p>Backend says: <strong>{data.hello}</strong></p>
                <p>
                    Edit <code>src/App.tsx</code> to add your frontend logic.
                </p>
                <p>
                    Edit <code>backend/main.py</code> to add your backend logic.
                </p>
            </div>

            {/* Add your components here */}
        </div>
    );
}

function App() {
    return (
        <ApolloProvider client={client}>
            <Content />
        </ApolloProvider>
    );
}

export default App;
