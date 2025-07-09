# Simple MBTI Test

questions = [
    {
        'dimension': 'EI',
        'prompt': '1. When meeting new people, do you (A) enjoy starting conversations or (B) prefer to wait for others to approach?',
        'A': 'E',
        'B': 'I'
    },
    {
        'dimension': 'EI',
        'prompt': '2. In social situations, do you (A) gain energy from being with others or (B) need time alone to recharge?',
        'A': 'E',
        'B': 'I'
    },
    {
        'dimension': 'EI',
        'prompt': '3. Do you prefer (A) group activities or (B) solitary activities?',
        'A': 'E',
        'B': 'I'
    },
    {
        'dimension': 'EI',
        'prompt': '4. When working on projects, do you (A) talk through ideas out loud or (B) think things through privately?',
        'A': 'E',
        'B': 'I'
    },
    {
        'dimension': 'EI',
        'prompt': '5. At parties, do you (A) mingle with many, including strangers, or (B) stick with a few people you know?',
        'A': 'E',
        'B': 'I'
    },
    {
        'dimension': 'SN',
        'prompt': '6. Do you focus on (A) facts and details or (B) patterns and possibilities?',
        'A': 'S',
        'B': 'N'
    },
    {
        'dimension': 'SN',
        'prompt': '7. When learning, do you prefer (A) practical applications or (B) abstract theories?',
        'A': 'S',
        'B': 'N'
    },
    {
        'dimension': 'SN',
        'prompt': '8. In planning a trip, do you rely on (A) specific itineraries or (B) exploring spontaneously?',
        'A': 'S',
        'B': 'N'
    },
    {
        'dimension': 'SN',
        'prompt': '9. When giving directions, do you (A) provide step-by-step instructions or (B) describe general landmarks?',
        'A': 'S',
        'B': 'N'
    },
    {
        'dimension': 'SN',
        'prompt': '10. Do you trust (A) experience more or (B) inspiration and imagination?',
        'A': 'S',
        'B': 'N'
    },
    {
        'dimension': 'TF',
        'prompt': '11. Are your decisions based more on (A) logic and consistency or (B) personal values and feelings?',
        'A': 'T',
        'B': 'F'
    },
    {
        'dimension': 'TF',
        'prompt': '12. Is it worse to be (A) unjust or (B) merciless?',
        'A': 'T',
        'B': 'F'
    },
    {
        'dimension': 'TF',
        'prompt': '13. Do you value (A) fairness and justice first or (B) empathy and harmony first?',
        'A': 'T',
        'B': 'F'
    },
    {
        'dimension': 'TF',
        'prompt': '14. When giving feedback, do you (A) focus on objective criteria or (B) consider the individual\'s feelings?',
        'A': 'T',
        'B': 'F'
    },
    {
        'dimension': 'TF',
        'prompt': '15. Are you more (A) analytical or (B) compassionate?',
        'A': 'T',
        'B': 'F'
    },
    {
        'dimension': 'JP',
        'prompt': '16. Do you prefer (A) planned and organized lifestyles or (B) flexible and spontaneous lifestyles?',
        'A': 'J',
        'B': 'P'
    },
    {
        'dimension': 'JP',
        'prompt': '17. When approaching deadlines, do you (A) work steadily in advance or (B) often rush at the last minute?',
        'A': 'J',
        'B': 'P'
    },
    {
        'dimension': 'JP',
        'prompt': '18. Do you find it easier to (A) make decisions or (B) keep options open?',
        'A': 'J',
        'B': 'P'
    },
    {
        'dimension': 'JP',
        'prompt': '19. Do you like (A) having a clear schedule or (B) going with the flow?',
        'A': 'J',
        'B': 'P'
    },
    {
        'dimension': 'JP',
        'prompt': '20. When finishing a project, do you (A) feel satisfaction from closure or (B) feel excitement for new possibilities?',
        'A': 'J',
        'B': 'P'
    }
]

analysis = {
    'ISTJ': {
        'desc': 'Responsible organizers who value traditions and loyalty.',
        'strengths': 'Dependable, detail-oriented, thorough.',
        'weaknesses': 'Can be rigid, may struggle with change.',
        'development': 'Practice flexibility and open-mindedness.'
    },
    'ISFJ': {
        'desc': 'Considerate caregivers who value harmony and cooperation.',
        'strengths': 'Supportive, practical, conscientious.',
        'weaknesses': 'May be overly selfless, dislike confrontation.',
        'development': 'Set healthy boundaries and share your needs.'
    },
    'INFJ': {
        'desc': 'Insightful advisors who seek meaning and deep connections.',
        'strengths': 'Empathetic, visionary, organized.',
        'weaknesses': 'Can be perfectionistic, may withdraw under stress.',
        'development': 'Balance idealism with realistic expectations.'
    },
    'INTJ': {
        'desc': 'Strategic thinkers who value competence and knowledge.',
        'strengths': 'Independent, analytical, determined.',
        'weaknesses': 'Can be critical, may struggle with emotion.',
        'development': 'Practice empathy and appreciate different viewpoints.'
    },
    'ISTP': {
        'desc': 'Adaptable troubleshooters who enjoy hands-on activities.',
        'strengths': 'Practical, resourceful, calm in crises.',
        'weaknesses': 'May be detached, dislike long explanations.',
        'development': 'Share your thoughts and connect with others.'
    },
    'ISFP': {
        'desc': 'Gentle caretakers who appreciate beauty and freedom.',
        'strengths': 'Warm, easygoing, artistic.',
        'weaknesses': 'Can avoid conflict, may be indecisive.',
        'development': 'Assert yourself and set clear goals.'
    },
    'INFP': {
        'desc': 'Thoughtful idealists who strive for authenticity and meaning.',
        'strengths': 'Creative, empathetic, loyal.',
        'weaknesses': 'Can be overly sensitive, perfectionistic.',
        'development': 'Balance ideals with practical action.'
    },
    'INTP': {
        'desc': 'Analytical problem solvers fascinated by concepts and ideas.',
        'strengths': 'Curious, objective, inventive.',
        'weaknesses': 'May seem distant, can overthink.',
        'development': 'Engage with others and test your theories.'
    },
    'ESTP': {
        'desc': 'Energetic doers who live in the present moment.',
        'strengths': 'Action-oriented, bold, realistic.',
        'weaknesses': 'Can be impulsive, may dislike routine.',
        'development': 'Plan ahead and consider long-term effects.'
    },
    'ESFP': {
        'desc': 'Playful performers who love excitement and socializing.',
        'strengths': 'Enthusiastic, friendly, resourceful.',
        'weaknesses': 'May avoid serious discussions, can be easily bored.',
        'development': 'Focus on responsibilities and future goals.'
    },
    'ENFP': {
        'desc': 'Imaginative motivators who see life as full of possibilities.',
        'strengths': 'Inspirational, flexible, compassionate.',
        'weaknesses': 'May be scattered, dislike routine.',
        'development': 'Prioritize tasks and follow through.'
    },
    'ENTP': {
        'desc': 'Inventive explorers who enjoy intellectual challenge.',
        'strengths': 'Quick-witted, outspoken, analytical.',
        'weaknesses': 'Can be argumentative, may lose interest quickly.',
        'development': 'Focus on completing projects and listening to others.'
    },
    'ESTJ': {
        'desc': 'Efficient organizers who value structure and order.',
        'strengths': 'Decisive, responsible, practical.',
        'weaknesses': 'May be inflexible, can overlook feelings.',
        'development': 'Consider others\' perspectives and emotions.'
    },
    'ESFJ': {
        'desc': 'Caring hosts who value cooperation and loyalty.',
        'strengths': 'Helpful, sociable, conscientious.',
        'weaknesses': 'May worry about approval, can be controlling.',
        'development': 'Take time for self-care and allow others freedom.'
    },
    'ENFJ': {
        'desc': 'Persuasive facilitators who thrive on helping others grow.',
        'strengths': 'Charismatic, empathetic, organized.',
        'weaknesses': 'Can be people-pleasing, may neglect own needs.',
        'development': 'Set boundaries and practice self-reflection.'
    },
    'ENTJ': {
        'desc': 'Commanding strategists who value efficiency and achievement.',
        'strengths': 'Confident, goal-oriented, strategic.',
        'weaknesses': 'May be impatient, can overlook feelings.',
        'development': 'Cultivate patience and attend to relationships.'
    }
}


def ask_questions():
    counts = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
    for q in questions:
        while True:
            print(q['prompt'])
            ans = input('Your choice (A/B): ').strip().upper()
            if ans in ('A', 'B'):
                counts[q[ans]] += 1
                break
            else:
                print('Please enter A or B.')
    return counts


def calculate_type(counts):
    result = ''
    dimensions = [('E', 'I'), ('S', 'N'), ('T', 'F'), ('J', 'P')]
    percentages = {}
    for a, b in dimensions:
        total = counts[a] + counts[b]
        if total == 0:
            pa = pb = 0
        else:
            pa = int(100 * counts[a] / total)
            pb = 100 - pa
        percentages[a + b] = {a: pa, b: pb}
        result += a if counts[a] >= counts[b] else b
    return result, percentages


def print_results(result_type, percentages):
    print('\nYour MBTI type is:', result_type)
    for pair, vals in percentages.items():
        letters = list(pair)
        print(f"{letters[0]}-{letters[1]}: {vals[letters[0]]}% {letters[0]}, {vals[letters[1]]}% {letters[1]}")
    info = analysis.get(result_type)
    if info:
        print('\nPersonality Analysis:')
        print(info['desc'])
        print('Strengths:', info['strengths'])
        print('Weaknesses:', info['weaknesses'])
        print('Personal Development:', info['development'])
    else:
        print('No detailed analysis available for this type.')


def main():
    print('Simple MBTI Test')
    print('Answer the following questions by selecting A or B.\n')
    counts = ask_questions()
    result_type, percentages = calculate_type(counts)
    print_results(result_type, percentages)


if __name__ == '__main__':
    main()
