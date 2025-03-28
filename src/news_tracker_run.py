import os
from resources import (
    extractUsernames,
    fetchXStats,
    saveApiResponse,
    updateAccounts,
    flagInvalidAccounts,
    updateProgress
)

def run(): 
    """
    Process accounts in batches of 100 per token, record the state for future executions. 
    """
    tokens = [os.getenv("X_BEARER_TOKEN_1"), os.getenv("X_BEARER_TOKEN_2"), os.getenv("X_BEARER_TOKEN_3")]
    for token in tokens:
        usernames = extractUsernames(useProgressFile=True)
        response = fetchXStats(",".join(usernames), token)
        print(response)
        if response:
            saveApiResponse(response)
            updateAccounts(response)
            flagInvalidAccounts(response)

            updateProgress(len(usernames))
        else:
            print('Error during the Response retrieval.')

if __name__ == "__main__":
    run()