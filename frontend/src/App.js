function App() {
    const LIST_OF_QUESTIONS = [
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
    function handleSubmit(event) {
        event.preventDefault()
        let res = []
        for (let i = 0; i < event.target.length - 1; i++) {
            res.push(event.target[i].value)
        }
        console.log(res)
    }

    return (
        <div className="App">
            <p>
                <b>Instructions</b> In the form below, for each statement 1-50
                mark how much you agree with on the scale 0-4, where 0=disagree,
                1=slightly disagree, 2=neutral, 3=slightly agree and 4=agree, in
                the box to the below it.
            </p>
            <form onSubmit={handleSubmit}>
                <p>I...</p>
                {LIST_OF_QUESTIONS.map((question, index) => {
                    return (
                        <div>
                            <label>{question}</label>
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
                <input type="submit"></input>
            </form>
        </div>
    )
}

export default App
