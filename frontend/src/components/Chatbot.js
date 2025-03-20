import { useEffect, useRef, useState } from "react";
import './Chatbot.css';
import "bootstrap-icons/font/bootstrap-icons.css";
import 'react-toastify/dist/ReactToastify.css';
import { toast } from "react-toastify";

function Chatbot() {
    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const chatboxRef = useRef(null);

    useEffect(() => {
        setTimeout(() => {
            setMessages([{ text: "Hey there! How can I help you?", sender: "bot" }]);
        }, 2000);
    }, []);

    useEffect(() => {
        if (chatboxRef.current) {
            chatboxRef.current.scrollIntoView({ behavior: "smooth" });
        }
    }, [messages]);

    const handleChat = async () => {
        if (!question.trim()) return;
        const userMessage = { text: question, sender: "user" };
        setMessages((prevMessages) => [...prevMessages, userMessage]);
        setIsLoading(true);

        try {
            const response = await fetch("/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                // mode: "no-cors",
                body: JSON.stringify({ query:question }) // ✅ Fixed request body format
            });

            if (!response.ok) {
                throw new Error(`Server Error: ${response.status}`);
            }

            const data = await response.json(); // ✅ Properly parsing JSON response
            const botReply = data.response || "Sorry, I couldn't process that."; // ✅ Extract response correctly

            const botMessage = { text: botReply, sender: "bot" };
            setMessages((prevMessages) => [...prevMessages, botMessage]);
            setQuestion("");
        } catch (error) {
            toast.error(error.message || "Something went wrong!");
        } finally {
            setIsLoading(false);
            setQuestion("");
        }
    };

    return (
        <div className="chat-container">
            <h1>Chatbot</h1>
            <div className="chat-box">
                {messages.map((message, index) => (
                    <div
                        key={index}
                        className={`message ${message.sender}`}
                        ref={index === messages.length - 1 ? chatboxRef : null}
                    >
                        {message.text}
                    </div>
                ))}
            </div>
            <div className="input-area">
                <input
                    type="text"
                    placeholder="Ask something..."
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    onKeyDown={(e) => e.key === "Enter" && handleChat()}
                />
                <button onClick={handleChat} disabled={isLoading}>
                    <i className={`bi bi-arrow-up-circle-fill ${isLoading ? "loading" : ""}`}></i>
                </button>
            </div>
        </div>
    );
}

export default Chatbot;
