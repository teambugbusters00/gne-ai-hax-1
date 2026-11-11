# GenAI Hackathon Copilot

FastAPI endpoint that provides a lightweight heuristic rubric-coverage score for a prompt and response.

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open /docs. This score is a debugging aid, not a reliable model-quality metric; use expert review and task-specific evaluation sets.

## Live deployment

- **Frontend:** https://gne-ai-hax-1-frontend-vijayjangids-projects.vercel.app
- **Backend API:** https://genai-hackathon-copilot-api.onrender.com
- **API docs:** https://genai-hackathon-copilot-api.onrender.com/docs

> Deployment is an MVP. Configure required secrets (if any), add authentication, and use durable database storage before production use.
