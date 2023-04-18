import { useState } from "react"

function App() {
    const LIST_OF_QUESTIONS1 = [
        "1. Am the life of the party:",
        "2. Feel little concern for others:",
        "3. Am always prepared:",
        "4. Get stressed out easily:",
        "5. Have a rich vocabulary:",
        "6. Don't talk a lot:",
        "7. Am interested in people:",
        "8. Leave my belongings around:",
        "9. Am relaxed most of the time:",
        "10. Have difficulty understanding abstract ideas:",
        "11. Feel comfortable around people:",
        "12. Insult people:",
        "13. Pay attention to details:",
        "14. Worry about things:",
        "15. Have a vivid imagination:",
        "16. Keep in the background:",
        "17. Sympathize with others' feelings:",
        "18. Make a mess of things:",
        "19. Seldom feel blue:",
        "20. Am not interested in abstract ideas:",
        "21. Start conversations:",
        "22. Am not interested in other people's problems:",
        "23. Get chores done right away:",
        "24. Am easily disturbed:",
        "25. Have excellent ideas:",
    ]
    const LIST_OF_QUESTIONS2 = [
        "26. Have little to say:",
        "27. Have a soft heart:",
        "28. Often forget to put things back in their proper place:",
        "29. Get upset easily:",
        "30. Do not have a good imagination:",
        "31. Talk to a lot of different people at parties:",
        "32. Am not really interested in others:",
        "33. Like order:",
        "34. Change my mood a lot:",
        "35. Am quick to understand things:",
        "36. Don't like to draw attention to myself:",
        "37. Take time out for others:",
        "38. Shirk my duties:",
        "39. Have frequent mood swings:",
        "40. Use difficult words:",
        "41. Don't mind being the center of attention:",
        "42. Feel others' emotions:",
        "43. Follow a schedule:",
        "44. Get irritated easily:",
        "45. Spend time reflecting on things:",
        "46. Am quiet around strangers:",
        "47. Make people feel at ease:",
        "48. Am exacting in my work:",
        "49. Often feel blue:",
        "50. Am full of ideas:",
    ]
    const [recommendations, setRecommendations] = useState([])

    function handleSubmit(event) {
        event.preventDefault()
        const res = []
        for (let i = 0; i < event.target.length - 1; i++) {
            res.push(parseInt(event.target[i].value))
        }
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ Answers: res }),
        }
        fetch("/recommend", requestOptions)
            .then((response) => response.json())
            .then((data) => setRecommendations(data))
    }

    return (
        <div className="App">
            <p>
                <b>Instructions</b> In the form below, for each statement 1-50
                mark how much you agree with on the scale 0-4, where 0=disagree,
                1=slightly disagree, 2=neutral, 3=slightly agree and 4=agree, in
                the box next to it. You will get an ordered list of
                recommendations at the bottom of the page.
            </p>
            <form onSubmit={handleSubmit}>
                <p>
                    <b>I...</b>
                </p>
                <div style={{ overflow: "auto" }}>
                    <div style={{ float: "left", paddingLeft: "100px" }}>
                        {LIST_OF_QUESTIONS1.map((question, index) => {
                            return (
                                <div style={{ padding: "5px" }}>
                                    <label style={{ paddingRight: "2px" }}>
                                        {question}
                                    </label>
                                    <select id={index}>
                                        <option value="0">0</option>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                    </select>
                                </div>
                            )
                        })}
                    </div>
                    <div style={{ float: "right", paddingRight: "100px" }}>
                        {LIST_OF_QUESTIONS2.map((question, index) => {
                            return (
                                <div style={{ padding: "5px" }}>
                                    <label style={{ paddingRight: "2px" }}>
                                        {question}
                                    </label>
                                    <select id={index}>
                                        <option value="0">0</option>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                    </select>
                                </div>
                            )
                        })}
                    </div>
                </div>
                <p>
                    <b>Room related questions: </b>
                </p>
                <div style={{ padding: "5px" }}>
                    <label style={{ paddingRight: "2px" }}>
                        What type of room do you want?
                    </label>
                    <select id>
                        <option value="0">2 People Room</option>
                        <option value="1">5 People Room</option>
                    </select>
                </div>
                <div style={{ padding: "5px" }}>
                    <label style={{ paddingRight: "2px" }}>
                        How important is it for you to get the type of room that
                        you want?
                    </label>
                    <select>
                        <option value="0">Low Importance</option>
                        <option value="1">Medium Importance</option>
                        <option value="2">High Importance</option>
                    </select>
                </div>
                <input type="submit" style={{ padding: "5px" }}></input>
            </form>
            <p>
                <b>List of Recommendations: </b>
            </p>
            <div>
                {recommendations.map((room) => {
                    return <div style={{ padding: "5px" }}>Room {room}</div>
                })}
            </div>
        </div>
    )
}

export default App
