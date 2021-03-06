import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.sanfoundry.com/engineering-mathematics-questions-answers-existence-laplace-transforms-some-elementary-functions-1/',
    'https://www.sanfoundry.com/engineering-mathematics-questions-answers-aptitude-test/',
    'https://www.sanfoundry.com/engineering-mathematics-questions-answers-laplace-transform-properties-1/',
    'https://www.sanfoundry.com/engineering-mathematics-questions-answers-campus-interviews/',
    'https://www.sanfoundry.com/engineering-mathematics-questions-answers-laplace-transform-properties-3/',
    'https://www.sanfoundry.com/ordinary-differential-equations-questions-answers-laplace-transform-periodic-function/',
    'https://www.sanfoundry.com/ordinary-differential-equations-questions-answers-general-properties-inverse-laplace-transform/',
    'https://www.sanfoundry.com/laplace-transform-questions-answers-convolution/',
    'https://www.sanfoundry.com/ordinary-differential-equations-multiple-choice-questions-answers/',
    'https://www.sanfoundry.com/ordinary-differential-equations-questions-answers-online-quiz/',
    'https://www.sanfoundry.com/fourier-analysis-questions-answers-fourier-series-expansions/',
    'https://www.sanfoundry.com/fourier-analysis-questions-answers-fourier-half-range-series/',
    'https://www.sanfoundry.com/partial-differential-equations-questions-answers-first-order-pde/',
    'https://www.sanfoundry.com/partial-differential-equations-questions-answers-first-order-linear-pde/',
    'https://www.sanfoundry.com/partial-differential-equations-questions-answers-first-order-non-linear-pde/',
    'https://www.sanfoundry.com/partial-differential-equations-assessment-questions-answers/',
    'https://www.sanfoundry.com/partial-differential-equations-questions-answers-experienced/',
    'https://www.sanfoundry.com/partial-differential-equations-questions-answers-solution-second-order-pde/',
    'https://www.sanfoundry.com/partial-differential-equations-questions-answers-entrance-exams/',
    'https://www.sanfoundry.com/fourier-analysis-interview-questions-answers-experienced/',
    'https://www.sanfoundry.com/partial-differential-equations-questions-answers-freshers/',
    'https://www.sanfoundry.com/partial-differential-equations-questions-bank/',
    'https://www.sanfoundry.com/partial-differential-equations-questions-answers-derivation-solution-two-dimensional-wave-equation/',
    'https://www.sanfoundry.com/fourier-analysis-questions-answers-fourier-transform-convolution/',
    'https://www.sanfoundry.com/fourier-analysis-interview-questions-answers/',
]

i = 1
text = ''

for url in urls:
    print('Getting:\n', url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    div = soup.find('div', 'inside-article')

    # Getting next Link
    # for anchor in div.find_all( 'a', href=True ):
    #     if str( anchor ).__contains__( 'Next' ):
    #         urls.append( str( anchor[ 'href' ] ) )
    #         break

    for line in div.text.splitlines():
        if line != '' and line != 'advertisement':
            if not line.__contains__('Next') and not line.__contains__('Prev'):
                if line.__contains__('Post navigation'):
                    break

                if not line.__contains__('Sanfoundry') and not line.__contains__(
                        '1000+ Multiple Choice Questions') and not line.__contains__(
                    'Instagram') and not line.__contains__('Engineering Mathematics'):
                    if line[0].isnumeric():
                        if line.__contains__('.'):
                            text += '\n'
                            question = line[line.index('.') + 1:]
                            text += str(i) + '.' + question + '\n'
                            i += 1
                        else:
                            text += line + '\n'
                    else:
                        text += line + '\n'

file = open('mcqs-m3.rtf', 'w')
file.write(text)
file.close()

print('Done')
