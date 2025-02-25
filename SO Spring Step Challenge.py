{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c8c5caa3-c42b-4a9c-aa73-6499df0fffec",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dictionary to store team members and their steps/calories\n",
    "teams = {\n",
    "    \"Team 1\": {\n",
    "        \"members\": [\n",
    "            {\"name\": \"Ailidh Snook\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Ashleigh Wilcox\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Amber Vater\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Nicole Ashman\", \"steps\": 0, \"calories\": 0}\n",
    "        ],\n",
    "        \"team_total_steps\": 0,\n",
    "        \"team_total_calories\": 0\n",
    "    },\n",
    "    \"Team 2\": {\n",
    "        \"members\": [\n",
    "            {\"name\": \"Becky Lyons-Helps\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Nikki Cholod\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Sian Giles-Titcombe\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Felcy Fernandes\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Maggie Wilson\", \"steps\": 0, \"calories\": 0}\n",
    "        ],\n",
    "        \"team_total_steps\": 0,\n",
    "        \"team_total_calories\": 0\n",
    "    },\n",
    "    \"Team 3\": {\n",
    "        \"members\": [\n",
    "            {\"name\": \"Sarah Garlick\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Jane Long\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Mel Kidd\", \"steps\": 0, \"calories\": 0},\n",
    "            {\"name\": \"Rachel Reynolds\", \"steps\": 0, \"calories\": 0}\n",
    "        ],\n",
    "        \"team_total_steps\": 0,\n",
    "        \"team_total_calories\": 0\n",
    "    },\n",
    "    # Add other teams here in the same way...\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "0d7d7af0-8b7f-452e-8969-688f7bd9497b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_participant(team_name, participant_name, steps=0, calories=0):\n",
    "    if team_name in teams:\n",
    "        teams[team_name][\"members\"].append({\"name\": participant_name, \"steps\": steps, \"calories\": calories})\n",
    "        print(f\"Added {participant_name} to {team_name}\")\n",
    "    else:\n",
    "        print(\"Team not found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "b76fb4da-b784-4b35-b384-9a98807611ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "def update_team_totals(team_name):\n",
    "    if team_name in teams:\n",
    "        total_steps = sum([member[\"steps\"] for member in teams[team_name][\"members\"]])\n",
    "        total_calories = sum([member[\"calories\"] for member in teams[team_name][\"members\"]])\n",
    "        \n",
    "        teams[team_name][\"team_total_steps\"] = total_steps\n",
    "        teams[team_name][\"team_total_calories\"] = total_calories\n",
    "        print(f\"Updated totals for {team_name}: {total_steps} steps, {total_calories} calories.\")\n",
    "    else:\n",
    "        print(\"Team not found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c0320912-5cec-4e9f-b66c-23fa27e6637c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_participant_with_image(team_name, participant_name, image_path, steps=0, calories=0):\n",
    "    if team_name in teams:\n",
    "        teams[team_name][\"members\"].append({\n",
    "            \"name\": participant_name,\n",
    "            \"image_path\": image_path,\n",
    "            \"steps\": steps,\n",
    "            \"calories\": calories\n",
    "        })\n",
    "        print(f\"Added {participant_name} to {team_name} with image {image_path}\")\n",
    "    else:\n",
    "        print(\"Team not found.\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3782b13-4a0e-4265-91c2-652eb187658d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
